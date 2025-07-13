import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1) # needed for url_for to generate with https

# configure the database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///portfolio.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# initialize the app with the extension, flask-sqlalchemy >= 3.0.x
db.init_app(app)

with app.app_context():
    # Make sure to import the models here or their tables won't be created
    import models  # noqa: F401
    db.create_all()
    
    # Initialize sample blog posts if none exist
    if models.BlogPost.query.count() == 0:
        sample_posts = [
            {
                'title': 'The Evolution of Mobile Gaming: Lessons from Real Cricket 20',
                'content': '''During my time at Nautilus Mobile App, I had the privilege of working on Real Cricket 20, one of the most acclaimed cricket games on mobile platforms. This experience taught me invaluable lessons about mobile game optimization and user engagement.

The challenge of implementing the "Highlights" feature was particularly interesting. We needed to create a system that could capture and replay the most exciting moments of a match while maintaining smooth performance across a wide range of Android and iOS devices.

Key takeaways from this project:
1. Performance optimization is crucial for mobile games
2. User feedback drives feature development
3. Cross-platform consistency requires careful planning
4. Memory management in Unity for mobile platforms

The "Challenge mode" feature also presented unique design challenges, requiring us to balance difficulty progression with player retention. We implemented a dynamic difficulty adjustment system that analyzed player performance and adjusted challenges accordingly.''',
                'excerpt': 'Insights from developing features for one of the most popular cricket games on mobile platforms.'
            },
            {
                'title': 'Blockchain Integration in Gaming: Building the Future with NFTs',
                'content': '''At Joyride Games, I was responsible for developing and maintaining an in-house SDK that allows easy integration of blockchain tokens and NFTs into any game. This project opened my eyes to the potential of blockchain technology in gaming.

The SDK needed to handle multiple blockchain networks, manage wallet connections, and provide a seamless user experience for players who might not be familiar with cryptocurrency. We focused on abstracting the complexity while maintaining security and transparency.

Challenges we solved:
- Cross-chain compatibility
- Gas fee optimization
- User experience design for non-crypto users
- Smart contract integration
- Real-time transaction monitoring

Working on Super Champs: Racket Rampage alongside the SDK development gave us real-world testing scenarios. The game's success validated our approach to blockchain integration in traditional gaming experiences.''',
                'excerpt': 'How we built an SDK to seamlessly integrate blockchain technology into traditional gaming experiences.'
            },
            {
                'title': 'From 2D to VR: The Technical Challenges of Multi-Platform Development',
                'content': '''My journey in game development has taken me across various platforms and dimensions - from 2D mobile games to VR experiences on HTC Vive. Each platform presents unique challenges and opportunities.

During my time at Driya Interactive, I worked on a forklift simulator prototype for HTC Vive. This project required completely rethinking user interaction paradigms and spatial design principles. The transition from traditional screen-based interfaces to 3D spatial computing was both challenging and rewarding.

Platform-specific considerations:
- VR: Comfort, motion sickness prevention, spatial audio
- Mobile: Touch controls, battery optimization, varying screen sizes
- Desktop: Precision controls, graphics scalability
- TV: Couch gaming, simplified UI, family-friendly interactions

The key to successful multi-platform development is understanding the unique strengths and limitations of each platform, then designing experiences that feel native rather than ported.''',
                'excerpt': 'Exploring the technical and design challenges of developing games across VR, mobile, and desktop platforms.'
            }
        ]
        
        for post_data in sample_posts:
            post = models.BlogPost(
                title=post_data['title'],
                content=post_data['content'],
                excerpt=post_data['excerpt']
            )
            db.session.add(post)
        
        db.session.commit()

# Import routes after app creation
import routes  # noqa: F401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
