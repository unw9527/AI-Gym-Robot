def generate_html_random():
    import random 
    import os
    import re
    from datetime import datetime, timedelta


   
    

                

    # Generate a random number of images between 1 and 10
    # Parse the log file and extract the necessary information
    log_file_path = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/logs/feedback.log"
    with open(log_file_path, "r") as file:
        log_lines = file.readlines()

    first_line = log_lines[0]
    exercise_type = ("push-up" in first_line)   #0 means squat, 1 means push up
    
    if(exercise_type):
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
            <h1>Welcome to Exercise Report</h1>
            
            <p>There are problems with the {problematic_push_ups_str}th push-ups.</p>
            <p>Total push-ups done: {total_push_ups}</p>
            <p>Total used time: {used_time}</p>
                    
            <p>Below are some of the screenshots of your improper gestures</p>
            {images}
        </body>
        </html>
        """
        problematic_push_ups = []
        total_push_ups = 0
        start_time = None
        end_time = None

        for line in log_lines:
            if "Starting to do push-up" in line:
                start_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Finish exercising" in line:
                end_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Push-up" in line and "done" in line:
                total_push_ups += 1
            elif "WARNING" in line:
                push_up_number = int(re.search(r"Push-up (\d+)", line).group(1))
                if push_up_number not in problematic_push_ups:
                    problematic_push_ups.append(push_up_number)

        problematic_push_ups_str = ', '.join(map(str, problematic_push_ups))
        used_time = end_time - start_time
    else:
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
            <h1>Welcome to Exercise Report</h1>
            
            <p>There are problems with the {problematic_push_ups_str}th squats.</p>
            <p>Total squats done: {total_push_ups}</p>
            <p>Total used time: {used_time}</p>
                    
            <p>Below are some of the screenshots of your improper gestures</p>
            {images}
        </body>
        </html>
        """
        problematic_push_ups = []
        total_push_ups = 0
        start_time = None
        end_time = None

        for line in log_lines:
            if "Starting to do squat" in line:
                start_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Finish exercising" in line:
                end_time = datetime.strptime(line.split(" ")[0] + " " + line.split(" ")[1], "%Y-%m-%d %H:%M:%S,%f")
            elif "Squat" in line and "done" in line:
                total_push_ups += 1
            elif "WARNING" in line:
                push_up_number = int(re.search(r"Squat (\d+)", line).group(1))
                if push_up_number not in problematic_push_ups:
                    problematic_push_ups.append(push_up_number)

        problematic_push_ups_str = ', '.join(map(str, problematic_push_ups))
        used_time = end_time - start_time
        
    
   


    # Set the image source, alt text, and width
    # image_src = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/website/imgs/covid.jpg"
    image_alt = "Example image"
    image_width = "500"
    # Define the directory containing the images
    image_directory = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/screenshots"

    # List all files in the directory
    all_files = os.listdir(image_directory)

    # Filter the list to include only image files (assuming they have .jpg, .jpeg, .png, or .gif extensions)
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    image_files = [file for file in all_files if any(file.endswith(ext) for ext in image_extensions)]

    num_images = random.randint(3, 4)
    # Randomly pick an image file
    # random_image = random.choice(image_files,num_images)
    random_image = random.sample(image_files,num_images)

    # Create the image elements in a loop
    images = ""
    for i in range(num_images):
        image_src = os.path.join(image_directory, random_image[i])
        # print("current image source: ",image_src,"\n")
        images += f'<img src="{image_src}" alt="{image_alt} {i+1}" width="{image_width}">\n'

    # Insert the content into the HTML template
    html_content = html_template.format(
        images=images,
        problematic_push_ups_str = problematic_push_ups_str,
        used_time = used_time,
        total_push_ups = total_push_ups
    )

    # Save the generated HTML content to a file
    with open("website/generated_random.html", "w") as file:
        file.write(html_content)

