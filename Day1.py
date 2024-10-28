import streamlit as st

# Main Title and Day Selector
st.title("365 Days of Code - Beginner to Super-Advanced")
day = st.selectbox("Select Day", ["Day 1: Hello World CLI Tool"])

if day == "Day 1: Hello World CLI Tool":
    st.header("Task Description")
    st.write("""
        **Objective**: Create a command-line tool that prints "Hello, World!" based on user input.
        By the end of the day, you should have a functioning CLI tool that displays the classic "Hello, World!" message.
    """)

    st.header("Concepts and Knowledge")
    st.subheader("Command-Line Interface (CLI)")
    st.write("""
        - **CLI Basics**: A Command-Line Interface (CLI) is a text-based user interface used to interact with software.
        - **Basic Input and Output**: Learn to take user input and print output to the console.
    """)

    st.header("Step-by-Step Guidance")
    st.write("""
        Follow these steps to build your first CLI tool:
    """)
    st.markdown("1. **Set up your environment**: Make sure Python is installed and a text editor is ready.")
    st.markdown("2. **Create a Python file**: Name it `hello_world.py`.")
    st.markdown("3. **Write the code**:")
    
    st.code("""
# hello_world.py
def main():
    user_input = input("Enter a greeting: ")
    print(f"{user_input}, World!")
    
if __name__ == "__main__":
    main()
    """, language="python")

    st.write("""
    - **Explanation**:
        - `input()`: Prompts the user for a greeting.
        - `print()`: Prints the user's greeting followed by ", World!".
    """)

    st.markdown("4. **Run your program**: Open the terminal, navigate to your script, and type:")
    st.code("python hello_world.py", language="bash")
    
    st.header("Code Snippets")

    st.code("""
def main():
    user_input = input("Enter a greeting: ")
    print(f"{user_input}, World!")
    
if __name__ == "__main__":
    main()
    """, language="python")

    st.write("""
    **Tips**:
    - Make sure you handle basic errors, such as if the user doesn’t enter anything.
    - Experiment by changing `user_input` to see how it affects the output.
    """)

    st.header("Notes")
    st.write("""
    - This project is foundational. It’s about familiarizing yourself with the CLI and basic Python functions.
    - Don’t worry if it feels simple; understanding these basics will help in more advanced projects.
    """)

### **Scalability Suggestions**

1. **Expandable Day Selector**: Use `selectbox` or `radio` buttons to add more days, each linked to unique project content.
2. **Project Templates**: For scalability, build a template function for each day’s layout.
3. **Separate Code Files**: Store each day’s guide in separate code files, which can be dynamically loaded based on the selected day.

This setup ensures clarity for Day 1 and is easily expandable for subsequent days, allowing a student to progress step-by-step through 365 unique projects.
