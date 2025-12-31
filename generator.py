from prompt_templates import image_prompt_template

print("=== AI Prompt Generator for Designers ===")

subject = input("Enter subject (e.g., Indian woman portrait): ")
style = input("Enter style (e.g., digital painting, cinematic): ")
mood = input("Enter mood (e.g., calm, dramatic): ")
lighting = input("Enter lighting (e.g., soft light, studio light): ")
color_palette = input("Enter color palette (e.g., warm tones, pastel): ")

final_prompt = image_prompt_template(
    subject,
    style,
    mood,
    lighting,
    color_palette
)

print("\nGenerated Prompt:\n")
print(final_prompt)
