import random
import time

def get_random_paragraph():
    # Replace this with a longer text passage if desired
    paragraph = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. 
    Sed sed turpis sed felis dignissim fringilla at eu libero. Nulla facilisi. 
    Quisque quis nibh nec mi auctor vulputate. Fusce eget diam at est vestibulum feugiat.
    """
    return paragraph.strip()

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")
    paragraph = get_random_paragraph()
    
    print("Type the following passage as fast as you can:\n")
    print(paragraph)
    
    input("Press Enter when you're ready to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    # Remove punctuation and split the text into words
    paragraph_words = paragraph.lower().strip().split()
    user_words = user_input.lower().strip().split()
    
    correct_words = 0
    for i in range(min(len(paragraph_words), len(user_words))):
        if user_words[i] == paragraph_words[i]:
            correct_words += 1
    
    elapsed_time = end_time - start_time
    wpm = (correct_words / elapsed_time) * 60
    
    print(f"\nWords per Minute (WPM): {wpm:.2f}")
    print(f"Correct Words: {correct_words}/{len(paragraph_words)}")

if __name__ == "__main__":
    typing_speed_test()
