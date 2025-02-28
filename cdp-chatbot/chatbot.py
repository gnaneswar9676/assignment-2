from document_indexer import DocumentIndexer


class CDPChatbot:
    def __init__(self):
        self.indexer = DocumentIndexer()
        self.indexer.build_index()
        self.platforms = ["Segment", "mParticle", "Lytics", "Zeotap"]

    def detect_platform(self, question):
        question = question.lower()
        detected = None
        for platform in self.platforms:
            if platform.lower() in question:
                detected = platform
                break
        return detected

    def handle_how_to(self, question):
        platform = self.detect_platform(question)
        if not platform:
            return "Which CDP are you asking about? I support Segment, mParticle, Lytics, and Zeotap."
        results = self.indexer.search(question)
        if isinstance(results, str):
            return results
        return f"For {platform}: {results.get(platform, 'No specific steps found in the docs.')}"

    def handle_comparison(self, question):
        platforms_mentioned = [p for p in self.platforms if p.lower() in question.lower()]
        if len(platforms_mentioned) < 2:
            return "Please mention at least two CDPs to compare (e.g., 'Segment vs Lytics')."
        results = self.indexer.search(question)
        response = "Comparison:\n"
        for platform in platforms_mentioned:
            info = results.get(platform, "No specific info found.")
            response += f"- {platform}: {info}\n"
        return response

    def process_question(self, question):
        question = question.strip()
        if not question:
            return "Please ask a question!"
        if "how" in question.lower():
            return self.handle_how_to(question)
        elif "compare" in question.lower() or "vs" in question.lower():
            return self.handle_comparison(question)
        else:
            return "I’m here for CDP-related 'how-to' or comparison questions. Try 'How do I set up a source in Segment?'"