def generate_html_random():
    import random 
    import os
    import re
    from datetime import datetime, timedelta



    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Exercise Report</title>
        <style>
            body {{
                font-size: 24px;
                text-align: center;
            }}
            
            img {{
                display: block;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <h1>{header_text}</h1>
        <p>Exercise Type: {exercise_display}</p>
        <p>There are problems with the {problematic_move_str}th {exercise_display}.</p>
        <p>Total {exercise_display} done: {total_counts}</p>
        <p>Total used time: {used_time}</p>
                
        <p>{paragraph_text}</p>
        {images}
    </body>
    </html>
    """



    header_text = "Welcome to Exercise Report"
    paragraph_text = "Below are some of the screenshots of your improper gestures"

    # Generate a random number of images between 1 and 10
    # Parse the log file and extract the necessary information
    log_file_path = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/logs/feedback.log"
    with open(log_file_path, "r") as file:
        log_lines = file.readlines()
        
    first_line = log_lines[0]
    exercise_type = ("push-up" in first_line) 
    if(exercise_type==1):
        exercise_display = "Push-Up"
    else:
        exercise_display = "Squat"
     
    problematic_moves = []
    total_counts = 0
    start_time = None
    end_time = None

    if(exercise_type==1):
        for line in log_lines:
            if "Starting to do push-up" in line:
                start_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            # elif "Finish exercising" in line:
            #     end_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Push-up" in line and "done" in line:
                total_counts += 1
            elif "WARNING" in line:
                push_up_number = int(re.search(r"Push-up (\d+)", line).group(1))
                if push_up_number not in problematic_moves:
                    problematic_moves.append(push_up_number)
    else: 
        for line in log_lines:
            if "Starting to do squat" in line:
                start_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            # elif "Finish exercising" in line:
            #     end_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Squat" in line and "done" in line:
                total_counts += 1
            elif "WARNING" in line:
                push_up_number = int(re.search(r"Squat (\d+)", line).group(1))
                if push_up_number not in problematic_moves:
                    problematic_moves.append(push_up_number)
    last_line = log_lines[-1]
    # print(last_line)
    end_time = datetime.strptime(last_line.split(" ")[0] + " " + last_line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
    problematic_move_str = ', '.join(map(str, problematic_moves))
    used_time = end_time - start_time
    
    # Set the image source, alt text, and width
    # image_src = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/website/imgs/covid.jpg"
    image_alt = "Example image"
    image_width = "500"
    images = ""
    # Define the directory containing the images
    image_directory = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/screenshots"
    # List all files in the directory
    all_files = os.listdir(image_directory)
    
    if(len(all_files)==0):
        paragraph_text = "All your moves are perfect! Nice!"
    else:
        # Filter the list to include only image files (assuming they have .jpg, .jpeg, .png, or .gif extensions)
        image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
        image_files = [file for file in all_files if any(file.endswith(ext) for ext in image_extensions)]

        upper = min(6,len(all_files))
        lower = int(len(all_files)/2)
        num_images = random.randint(lower, upper)
        # Randomly pick an image file
        # random_image = random.choice(image_files,num_images)
        random_image = random.sample(image_files,num_images)
        # Create the image elements in a loop
        
        for i in range(num_images):
            image_src = os.path.join(image_directory, random_image[i])
            # print("current image source: ",image_src,"\n")
            images += f'<img src="{image_src}" alt="{image_alt} {i+1}" width="{image_width}">\n'

     # Insert the content into the HTML template
    html_content = html_template.format(
        header_text=header_text,
        paragraph_text=paragraph_text,
        images=images,
        problematic_move_str = problematic_move_str,
        used_time = used_time,
        total_counts = total_counts,
        exercise_display=exercise_display
    )
    # Save the generated HTML content to a file
    with open("website/generated_random.html", "w") as file:
        file.write(html_content)