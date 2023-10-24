import os
from bs4 import BeautifulSoup
import re
import csv

# HTML content (replace with your actual HTML content)

def clean_and_extract_dialogues(file_path):
    with open(file_path, "r", encoding="utf-8") as file:

        # Pass the filehandle to Beautiful Soup for parsing
        soup = BeautifulSoup(file, 'html.parser')
        character_dialogue_pairs = []
        formatted_output = []

    # Find all <div> elements with class "npc"
    npc_elements = soup.find_all('div', class_='npc')

    # Iterate through the <div> elements
    for div_element in npc_elements:
        # Extract the character name from the <div> element
        character_name = div_element.get_text().strip()
        character_name = re.sub(r'\s+', ' ', character_name)

        # Find the <span> element with class "dialog" immediately following the <div>
        next_span = div_element.find_next('span', class_='dialog')

        if next_span:
            # Extract and format the dialogue line
            dialogue_text = next_span.get_text().strip()
            dialogue_text = re.sub(r'<br>','',dialogue_text)
            dialogue_text = re.sub(r'\s+', ' ', dialogue_text)
            formatted_line = f"{character_name}: {dialogue_text}"
            if len(character_name) < 30:
                formatted_output.append(formatted_line)


    # Join the formatted lines with line breaks
    formatted_text = '\n'.join(formatted_output)
    return formatted_output


# Specify the root folder where your HTML files are located
root_folder = r"C:\Users\cemea\Documents\BG3_-_parsed_dialogue_1.0-20230915T195130Z-001\BG3-parsedDialogue\Dialogs"

# Create an empty list to store all transcripts
all_transcripts = []

# Recursively traverse the directory tree using os.walk
for root, _, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)
            transcript = clean_and_extract_dialogues(file_path)
            all_transcripts.extend(transcript)


r"""
# Specify the output file path
output_file_path = 'output_transcript.txt'

# Write all transcripts to the output file
with open(r"C:\Users\cemea\Documents\BG3_-_parsed_dialogue_1.0-20230915T195130Z-001\BG3-parsedDialogue\output_text.txt", 'w', encoding='utf-8') as output_file:
    for transcript in all_transcripts:
   #     output_file.write(r"{transcript}\n00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvomb  ")
"""

# Specify the output CSV file path
output_csv_file = r'C:\Users\cemea\Documents\BG3_-_parsed_dialogue_1.0-20230915T195130Z-001\BG3-parsedDialogue\output_transcript.csv'

# Write all transcripts to the CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for transcript in all_transcripts:
        character, dialogue = transcript.split(': ', 1)
        csvwriter.writerow([character, dialogue])