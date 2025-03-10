import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*-3ufdqzjr)98^522xse6a^!28244ub=x9k1k9slbbd0jw)sa*"

os.environ.setdefault(
    "DATABASE_URL", 
    "postgresql://neondb_owner:npg_zvDqQC51olME@ep-old-silence-a2eqq6z9.eu-central-1.aws.neon.tech/igloo_spoon_mango_276652")
os.environ.setdefault('DEBUG', 'TRUE')
os.environ.setdefault("CLOUDINARY_URL", "cloudinary://664772432717391:wFr5MDgP0LcWBlAwByaSDjsLAMw")