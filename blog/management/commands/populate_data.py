from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Blog Poduven"
    def handle(self, *args, **options):
        blog_data = [
        {
            "id":"1",
            "title": "The Rise of AI: How It's Changing Everything",
            "content": "Artificial Intelligence is transforming industries, from healthcare to finance. Here's what you need to know about the AI revolution.",
            "img_url": "https://images.unsplash.com/photo-1697577418970-95d99b5a55cf?q=80&w=1992&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=600&q=80"
        },
        {
            "id":"2",
            "title": "Top 5 Programming Languages You Should Learn in 2025",
            "content": "Stay ahead in the tech industry by mastering these programming languages that are shaping the future.",
            "img_url": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=600&q=80"
        },
        {
            "id":"3",
            "title": "Why Cybersecurity Skills Are in High Demand",
            "content": "As threats increase online, companies are paying top dollar for cybersecurity professionals. Here's how to get started.",
            "img_url": "https://plus.unsplash.com/premium_photo-1674669009418-2643aa58b11b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=600&q=80"
        },
        {
            "id":"4",
            "title": "How Blockchain is Disrupting Traditional Finance",
            "content": "Blockchain isn't just about crypto. Learn how decentralized tech is reshaping global finance and business models.",
            "img_url": "https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&h=600&q=80"
        },
        {
            "id":"5",
            "title": "The Future of Web Development: Trends to Watch",
            "content": "From Web3 to AI-integrated frontends, the web is evolving rapidly. Explore the next big things in web development.",
            "img_url": "https://images.unsplash.com/photo-1571171637578-41bc2dd41cd2?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=600&q=80"
        }
    ]

        for blog in blog_data:
           Post.objects.create(title=blog["title"], content=blog["content"], img_url=blog["img_url"])

        self.stdout.write(self.style.SUCCESS("Completed !"))