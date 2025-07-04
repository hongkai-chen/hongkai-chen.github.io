def convert_author_names(input_file, output_file):
    """
    Convert author names from Eastern order (Last, First) to Western order (First Last)
    and ensure proper formatting with line breaks.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    new_lines = []
    for line in lines:
        line = line.rstrip()  # Remove trailing whitespace
        if line.strip().startswith('author='):
            # Extract the author line
            author_line = line.strip()
            # Find the position of the equals sign and the first brace
            eq_pos = author_line.find('=')
            start_brace = author_line.find('{', eq_pos)
            end_brace = author_line.rfind('}', start_brace)
            # Extract the authors string
            authors = author_line[start_brace+1:end_brace]
            # Split authors by ' and '
            authors_list = authors.split(' and ')
            # Convert each author name
            converted_authors = []
            for author in authors_list:
                parts = author.split(',')
                if len(parts) == 2:  # Ensure there is a comma to split on
                    converted_author = f"{parts[1].strip()} {parts[0].strip()}"
                    converted_authors.append(converted_author)
                else:
                    converted_authors.append(author)  # No comma, leave as is
            # Join converted authors back with ' and '
            new_authors = ' and '.join(converted_authors)
            # Replace the old authors string with the new one
            new_author_line = f"author = {{{new_authors}}},\n"
            new_lines.append(new_author_line)
        else:
            new_lines.append(line + '\n')  # Append line with newline character
    
    # Write the new content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Example usage
convert_author_names('input.bib', 'output.bib')

# def convert_author_names(input_file, output_file):
#     """
#     Convert author names from Eastern order (Last, First) to Western order (First Last).
#     """
#     with open(input_file, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
    
#     new_lines = []
#     for line in lines:
#         if line.strip().startswith('author'):
#             # Extract the author line
#             author_line = line.strip()
#             # Find the position of the equals sign and braces
#             eq_pos = author_line.find('=')
#             start_brace = author_line.find('{', eq_pos)
#             end_brace = author_line.find('}', start_brace)
#             # Extract the authors string
#             authors = author_line[start_brace+1:end_brace]
#             # Split authors by ' and '
#             authors_list = authors.split(' and ')
#             # Convert each author name
#             converted_authors = []
#             for author in authors_list:
#                 parts = author.split(', ')
#                 if len(parts) == 2:  # Ensure there is a comma to split on
#                     converted_author = f"{parts[1].strip()} {parts[0].strip()}"
#                     converted_authors.append(converted_author)
#                 else:
#                     converted_authors.append(author)  # No comma, leave as is
#             # Join converted authors back with ' and '
#             new_authors = ' and '.join(converted_authors)
#             # Replace the old authors string with the new one
#             new_author_line = f"{author_line[:start_brace+1]}{new_authors}{author_line[end_brace:]}"
#             new_lines.append(new_author_line)
#         else:
#             new_lines.append(line)
    
#     # Write the new content to the output file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.writelines(new_lines)

# # Example usage
# convert_author_names('input.bib', 'output.bib')