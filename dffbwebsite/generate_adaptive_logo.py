#!/usr/bin/env python3
"""Generate adaptive image formats (WebP, AVIF) from PNG source for logo."""

from pathlib import Path
from PIL import Image
import pillow_avif  # Register AVIF support

src = Path(__file__).parent / "dffb-logo.png"
if not src.exists():
    print(f"Source {src} not found")
    exit(1)

try:
    img = Image.open(src)
    print(f"Original: {img.format} {img.size}")
    
    # Generate WebP
    webp_path = src.stem + ".webp"
    img.save(webp_path, "WebP", quality=90)
    print(f"Generated: {webp_path} ({Path(webp_path).stat().st_size} bytes)")
    
    # Generate AVIF
    avif_path = src.stem + ".avif"
    img.save(avif_path, "AVIF", quality=90)
    print(f"Generated: {avif_path} ({Path(avif_path).stat().st_size} bytes)")
    
    # Keep PNG for reference
    png_size = src.stat().st_size
    print(f"Original: {src} ({png_size} bytes)")
    print("✓ Adaptive logo generation complete")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
