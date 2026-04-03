from app.services.rag import rag_engine
from app.services.eligibility import eligibility_engine
from app.services.recommendation import recommendation_engine
from app.utils.loader import loader
from app.models import SchemeResponse

class ChatbotEngine:
    def chat_pipeline(self, user_query: str, user_profile: dict = None):
        if not user_query:
            return {"response": "Hi there! I am your AI assistant. How can I help you find government schemes today?", "schemes": []}
            
        user_query_lower = user_query.lower()
        
        # 5. INTENT DETECTION (LIGHTWEIGHT)
        if "eligible" in user_query_lower or "eligibility" in user_query_lower:
            intent = "eligibility"
        elif "suggest" in user_query_lower or "recommend" in user_query_lower:
            intent = "recommendation"
        else:
            intent = "general"
            
        schemes_data = loader.schemes
        if not schemes_data:
            return {"response": "I'm currently unable to load our schemes database. Please try again soon.", "schemes": []}

        response_text = ""
        final_schemes = []

        # C. Recommendation Query
        if intent == "recommendation":
            if user_profile and any(user_profile.values()):
                # Use recommendation engine (Retrieval + Eligibility + Ranking)
                top_responses = recommendation_engine.get_recommendations(user_profile, {"query": user_query})
                
                # Check for empty fallback
                if top_responses and top_responses[0].scheme_name == "No Match Found":
                    response_text = "I couldn't find any schemes that closely align with your profile. You might consider adjusting your details or trying a broader search."
                else:
                    top_2 = top_responses[:2]
                    final_schemes = [s.model_dump() for s in top_responses]
                    
                    s1 = top_2[0] if len(top_2) > 0 else None
                    s2 = top_2[1] if len(top_2) > 1 else None
                    
                    response_text = "Based on your profile, here are my top suggestions: "
                    if s1:
                        response_text += f"\n\n**1. {s1.scheme_name}** - It provides {s1.benefits}. With a confidence score of {int(s1.confidence_score*100)}%, you are a {s1.match_type.lower()} match."
                    if s2:
                        response_text += f"\n**2. {s2.scheme_name}** - Another strong choice in the {s2.category} category."
            else:
                response_text = "To suggest the best schemes accurately, I need a bit more information. Could you please provide your profile details like age, income, state, or occupation?"

        # B. Eligibility Query
        elif intent == "eligibility":
            if user_profile and any(user_profile.values()):
                # Run retrieval to find the specific scheme
                faiss_results = rag_engine.search(user_query, top_k=3)
                if not faiss_results:
                    response_text = "I couldn't identify the specific scheme you're asking about. Can you clarify the name?"
                else:
                    target_scheme_id = faiss_results[0]["id"]
                    target_scheme = next((s for s in schemes_data if s.get("scheme_id") == target_scheme_id), None)
                    
                    if target_scheme:
                        is_el, conf, match_reason, match_type = eligibility_engine.evaluate(user_profile, target_scheme)
                        name = target_scheme.get("scheme_name", "this scheme")
                        
                        # 6. EXPLANATION ENGINE
                        if is_el:
                            response_text = f"Great news! You appear to be eligible for the **{name}**. {match_reason.split('.')[0]}."
                        else:
                            response_text = f"You might not currently meet all the criteria for the **{name}**. {match_reason.split('.')[0]}."
                        
                        categories = target_scheme.get("scheme_category", [])
                        cat_str = categories[0] if categories else "General"
                        benefits_obj = target_scheme.get("benefits", {})
                        benefits_text = benefits_obj.get("description", "benefits")
                        if benefits_obj.get('amount'):
                            benefits_text = f"{benefits_obj.get('amount')} - {benefits_text}"
                            
                        final_schemes.append(SchemeResponse(
                            scheme_name=name,
                            eligible=is_el,
                            confidence_score=conf,
                            match_reason=match_reason,
                            benefits=benefits_text,
                            application_link=target_scheme.get("application", {}).get("link", ""),
                            category=cat_str,
                            documents_required=target_scheme.get("documents_required", []),
                            match_type=match_type,
                            priority_tag="Standard"
                        ).model_dump())
            else:
                response_text = "To check your eligibility, I need to know a few details about you! What is your age, income, and occupation?"
                
        # A. General Query
        else:
            faiss_results = rag_engine.search(user_query, top_k=2)
            if not faiss_results:
                response_text = "I'm not exactly sure about that. Could you try rephrasing your question to include a specific scheme or topic like 'farmers'?"
            else:
                top_2_schemes = []
                for res in faiss_results:
                    sch = next((s for s in schemes_data if s.get("scheme_id") == res["id"]), None)
                    if sch: top_2_schemes.append(sch)
                
                if top_2_schemes:
                    s1 = top_2_schemes[0]
                    name1 = s1.get("scheme_name")
                    benefits_obj = s1.get("benefits", {})
                    ben1 = benefits_obj.get("description", "helpful support")
                    if benefits_obj.get("amount"):
                        ben1 = f"{benefits_obj.get('amount')} - {ben1}"
                    
                    response_text = f"I found some relevant information. **{name1}** provides {ben1}."
                    if len(top_2_schemes) > 1:
                        s2 = top_2_schemes[1]
                        name2 = s2.get("scheme_name")
                        response_text += f"\nThere's also **{name2}**, which might be helpful."
                    response_text += "\n\nWould you like me to check if you are eligible for these?"
                    
                    for sch in top_2_schemes:
                        categories = sch.get("scheme_category", [])
                        cat_str = categories[0] if categories else "General"
                        benefits_obj = sch.get("benefits", {})
                        benefits_text = benefits_obj.get("description", "")
                        if benefits_obj.get('amount'):
                            benefits_text = f"{benefits_obj.get('amount')} - {benefits_text}"
                            
                        final_schemes.append(SchemeResponse(
                            scheme_name=sch.get("scheme_name", "Unknown"),
                            eligible=True,
                            confidence_score=0.0,
                            match_reason="General inquiry result",
                            benefits=benefits_text,
                            application_link=sch.get("application", {}).get("link", ""),
                            category=cat_str,
                            documents_required=sch.get("documents_required", []),
                            match_type="Info",
                            priority_tag="Standard"
                        ).model_dump())

        return {"response": response_text, "schemes": final_schemes}

chatbot_engine = ChatbotEngine()
