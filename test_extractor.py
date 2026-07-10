from app.extractors.profile_extractor import ProfileExtractor

extractor = ProfileExtractor()

print(
    extractor.extract(
        "Hi, I'm Madhav from Patiala and I'm a Full Stack Developer."
    )
)