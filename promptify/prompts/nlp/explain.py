def Explain(
        context: str,  # the context paragraph
        domain: str = "",  # the domain of the question, optional
          ):
        """
        This function returns a template string with the input context. The template also includes a description of the function's purpose. If a domain is provided, it is
        included in the function's description.
        """
    
        if domain:
            template = f"You are a highly intelligent {domain} domain expert Explanation system. You take Passage as input and explain the passage as a {domain} expert, meaningful and accurate explanation. Your output format is only [{{'E': Explained paragraph}},] form, no other form.\n"
        else:
            template = "You are a highly intelligent Explanation system. You take Passage as input and explain the passage as an expert,meaningful and accurate explanation. Your output format is only [{'E': Explained paragraph},] form, no other form.\n"

        # add the input context and question to the template
        template += f"\nPassage: {context}\nOutput:"
        return template
