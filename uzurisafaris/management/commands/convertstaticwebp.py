import os
from django.conf import settings
from django.core.management.base import BaseCommand
from PIL import Image

class Command(BaseCommand):
    help = "Convert all static JPG/PNG images to WebP format"

    def add_arguments(self, parser):
        parser.add_argument(
            '--quality',
            type=int,
            default=80,
            help='Quality of WebP images (0-100, default=80)'
        )
        parser.add_argument(
            '--delete-original',
            action='store_true',
            help='Delete original JPG/PNG files after conversion'
        )

    def handle(self, *args, **options):
        quality = options['quality']
        delete_original = options['delete_original']

        static_dirs = [os.path.join(settings.BASE_DIR, "static")]

        for static_dir in static_dirs:
            if not os.path.exists(static_dir):
                self.stdout.write(self.style.ERROR(f"Static dir not found: {static_dir}"))
                continue

            for root, _, files in os.walk(static_dir):
                for file in files:
                    if file.lower().endswith((".jpg", ".jpeg", ".png")):
                        file_path = os.path.join(root, file)
                        webp_path = os.path.splitext(file_path)[0] + ".webp"

                        try:
                            img = Image.open(file_path).convert("RGB")
                            img.save(webp_path, "webp", quality=quality)
                            self.stdout.write(self.style.SUCCESS(f"Converted: {file_path} → {webp_path}"))

                            if delete_original:
                                os.remove(file_path)
                                self.stdout.write(self.style.WARNING(f"Deleted original: {file_path}"))

                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Failed {file_path}: {e}"))

        self.stdout.write(self.style.SUCCESS("✅ Static image conversion complete!"))
