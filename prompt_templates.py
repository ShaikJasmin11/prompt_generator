def image_prompt_template(
    subject,
    style,
    mood,
    lighting,
    color_palette,
    quality="ultra-detailed, high resolution, 8k"
):
    prompt = f"""
    A {subject},
    in {style} style,
    conveying a {mood} mood,
    with {lighting} lighting,
    using a {color_palette} color palette,
    {quality},
    sharp focus, professional composition,
    cinematic depth, highly realistic.
    """
    return " ".join(prompt.split())
