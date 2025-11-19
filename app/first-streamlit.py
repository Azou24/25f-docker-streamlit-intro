# Intro Streamlit Demo

import streamlit as st

# Function to create a sample data frame and display it
def expanded_app():
    st.title("Welcome to a Streamlit Demo! Alex!a🎈")
    
    # Navigation button to API Access page on the left menu bar
    st.page_link("pages/1_API_Access.py", label="Go to API Access", icon="🔌")
    
    
    #######################################################################
    ## --------------- IN CLASS ---------------
    # Let's personalize this a little.  Add in headshots or avatars for each of 
    # your team members present in class today. 
    st.header("About You & About Me")
    
    # Create two columns: one for the image, one for the bio
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display placeholder headshot image
        # Students should replace 'avatar.png' in assets/images/ with their own headshot
        st.image("assets/images/avatar.png", 
                 width=200, 
                 caption="Replace this image with your headshot in assets/images/")
    
    with col2:
        # Lorem ipsum placeholder text - Put a little Bio here!
        st.write("""
        **Lorem ipsum dolor sit amet**, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat.
        
        *Replace this lorem ipsum text with your own brief bio.*
        """)
    
    st.markdown("---")
     

    # ------- Displaying Text -------
    st.header("Text Presentation Showcase")

    st.subheader("Use `st.text()` for simple text:")
    st.text("This is a string of text displayed using st.text().")
    st.text("DS 3000 and CS 3200 are the best classes ever!")

    st.subheader("Using `st.markdown()` for rich text formatting:")
    st.markdown("""
        `st.markdown()` let's you embed markdown right in your output! 
        
        You can:
        * Make text **bold** or *italic*.
        * Create lists:
            * Unordered list item 1
            * Unordered list item 2
        * Or ordered lists:
            1.  Ordered list item 1
            2.  Ordered list item 2
        * Include [hyperlinks](https.streamlit.io).
        * Write blockquotes:
            > *To be, or not to be, that is the question.*
        * And even horizontal rules:
        ---
    """)

    st.subheader("Using `st.write()` with Markdown:")
    st.write("`st.write()` is a magic command and can also render Markdown!")
    st.write("### This is an H3 heading inside `st.write()`")
    st.write("You can **bold** text, use *italics*, and create lists:")
    st.write("- Item A from `st.write()`")
    st.write("- Item B from `st.write()`")
    st.write("1. Numbered item 1 from `st.write()`")
    st.write("2. Numbered item 2 from `st.write()`")
    st.write("Check out this link rendered by `st.write()`: [Streamlit Docs](https://docs.streamlit.io)")
    st.write("---")

    st.subheader("Displaying Headers and Subheaders:")
    st.header("This is an `st.header()`")
    st.subheader("This is an `st.subheader()`")
    st.caption("And this is `st.caption()`, useful for small text or image captions.")

    # ------ Other Data Display Elements -------
    st.header("More Data Display Options")

    # Using st.columns to display 3 metrics side by side.
    st.subheader("Use `st.metric()` to display key performance indicators (KPIs):")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Temperature", value="25 °C", delta="1.2 °C")
    col2.metric(label="Humidity", value="65%", delta="-2%")
    # Delta_color can be "normal", "inverse", or "off"
    col3.metric(label="Active Users", 
                value="1,203", 
                delta="102 since last week", 
                delta_color="off") 
    
    #######################################################################
    ## ----------------------- IN CLASS ----------------------- 
    # Change the metrics above to some user and application example metrics 
    # that you might actually use in your project UI.
    #######################################################################
    
    # ------ Markdown in st.write directly with variables ------
    st.header("Dynamic Markdown in `st.write`")
    st.write("""You can construct Markdown strings dynamically (adding 
             in vales from other variables) and pass them to `st.write()`.""")
    fruit_name = "Apple"
    fruit_color = "Red"
    fruit_quantity = 10

    # Notice the use of the formatted string f"""..."""
    markdown_string = f"""
    ### Fruit Inventory:

    We have **{fruit_quantity}** *{fruit_color}* _{fruit_name}_s.

    Here's a list:
    - **Name**: {fruit_name}
    - **Color**: {fruit_color}
    - **Quantity**: {fruit_quantity}
    """
    st.write(markdown_string)


# Call the expanded_app() function
if __name__ == "__main__":
    expanded_app()
