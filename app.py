import streamlit as st

# --------- Website Config ---------
st.set_page_config(page_title="Book Haven", page_icon="📚", layout="wide")
mode = st.sidebar.selectbox("🌓 Mode", ["Light", "Dark"])

if mode == "Dark":
    st.markdown("""
        <style>
        body, .stApp { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stApp { background-color: white; color: black; }
        </style>
    """, unsafe_allow_html=True)

# --------- Session State ---------
if "cart" not in st.session_state:
    st.session_state.cart = []
if "order_history" not in st.session_state:
    st.session_state.order_history = []
if "user" not in st.session_state:
    st.session_state.user = None

# --------- Sidebar ---------
st.sidebar.image("images/logo.png", width=120)
st.sidebar.title("📚 Book Haven")

if st.session_state.user:
    st.sidebar.success(f"👋 Welcome, {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()
else:
    with st.sidebar.expander("🔐 Login / Signup"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username and password:
                st.session_state.user = username
                st.success(f"Logged in as {username}")
                st.rerun()
            else:
                st.error("Please enter both username and password.")

# --------- Menu Selection ---------
page = st.sidebar.selectbox("Menu", ["Home", "Books", "Cart", "Orders", "Search", "Contact", "About"])

st.sidebar.markdown("---")
st.sidebar.subheader("🎁 Offers")
st.sidebar.markdown("""
- 🔥 50% off Comics  
- 🚀 Buy 2 Get 1 Free  
- 💡 Programming Guide @ ₹299  
""")

st.sidebar.subheader("📰 Newsletter")
email = st.sidebar.text_input("Enter your email")
if st.sidebar.button("Subscribe"):
    st.sidebar.success("Subscribed!")

st.sidebar.subheader("📞 Contact")
st.sidebar.markdown("""
🏠 No. 25, Gandhi Nagar, Thiruvarur – 610001  
📧 hello@bookhaven.in  
📞 +91 94444 12345  
""")

st.sidebar.subheader("🌐 Follow Us")
st.sidebar.markdown("""
[📸 Instagram](https://instagram.com/bookhaven_thiruvarur)  
[📘 Facebook](https://facebook.com/bookhavenTVR)  
[X](https://x.com/bookhaventvr)
""")

# --------- Book Data ---------
categories = ["All", "Comics", "Fiction", "Finance", "Programming", "Self Care"]
category_images = {
    "Comics": "images/Comics.png",
    "Fiction": "images/Fiction.png",
    "Programming": "images/Programming.png",
    "Finance": "images/Finance.png",
    "Self Care": "images/selfHelp.png"
}
books = [
    {"title": "1984", "author": "George Orwell", "price": "₹499", "image": "images/1984.jpg", "category": "Fiction", "description": "A dystopian novel about totalitarianism and surveillance."},
    {"title": "Atomic Habits", "author": "James Clear", "price": "₹499", "image": "images/AtomicHabits.jpg", "category": "Finance", "description": "Tiny habits lead to big results."},
    {"title": "Harry Potter", "author": "J.K. Rowling", "price": "₹699", "image": "images/harrypotter.jpg", "category": "Fiction", "description": "A magical adventure at Hogwarts."},
    {"title": "Ikigai", "author": "Héctor García", "price": "₹399", "image": "images/Ikigai.jpg", "category": "Self Care", "description": "Find your life's purpose the Japanese way."},
    {"title": "One Piece", "author": "Eiichiro Oda", "price": "₹450", "image": "images/OnePiece.jpg", "category": "Comics", "description": "A thrilling pirate journey with Luffy."},
    {"title": "Clean Code", "author": "Robert C. Martin", "price": "₹850", "image": "images/cleancode.jpg", "category": "Programming", "description": "Write clean and efficient code."},
    {"title": "Spiderman", "author": "Marvel", "price": "₹550", "image": "images/Spiderman.jpg", "category": "Comics", "description": "The friendly neighborhood hero's story."},
    {"title": "DC Comics", "author": "Melanie Scott", "price": "₹899", "image": "images/DC.jpg", "category": "Comics", "description": "Explore heroes from the DC Universe."},
    {"title": "Naruto", "author": "Masashi Kishimoto", "price": "₹399", "image": "images/Naruto.jpg", "category": "Comics", "description": "Ninja battles and dreams of Hokage."},
    {"title": "Attack on Titan", "author": "Hajime Isayama", "price": "₹450", "image": "images/aot.jpg", "category": "Comics", "description": "Survive in a world of titans."},
    {"title": "Demon Slayer", "author": "Koyoharu Gotouge", "price": "₹450", "image": "images/DemonSlayer.jpg", "category": "Comics", "description": "Fight demons with Tanjiro."},
    {"title": "Intro to ML", "author": "Andriy Burkov", "price": "₹899", "image": "images/IntroToML.jpg", "category": "Programming", "description": "A beginner's guide to machine learning."},
    {"title": "Design Patterns", "author": "Erich Gamma", "price": "₹799", "image": "images/DesignPatterns.jpg", "category": "Programming", "description": "Reusable software design concepts."},
    {"title": "Midnight Library", "author": "Matt Haig", "price": "₹550", "image": "images/MidnightLibrary.jpg", "category": "Fiction", "description": "A tale of second chances and choices."},
    {"title": "It Ends With Us", "author": "Colleen Hoover", "price": "₹499", "image": "images/ItEndsWithUs.jpg", "category": "Fiction", "description": "An emotional story of love and heartbreak."},
    {"title": "Can't Hurt Me", "author": "David Goggins", "price": "₹599", "image": "images/canthurtme.jpg", "category": "Self Care", "description": "Master your mind and defy the odds."},
    {"title": "Deep Work", "author": "Cal Newport", "price": "₹649", "image": "images/DeepWork.jpg", "category": "Self Care", "description": "Rules for focused success in a distracted world."},
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": "₹499", "image": "images/alchemist.jpg", "category": "Fiction", "description": "Follow your dreams and listen to your heart."},
    {"title": "Percy Jackson", "author": "Rick Riordan", "price": "₹550", "image": "images/percy.jpg", "category": "Fiction", "description": "Greek mythology and adventure collide."},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "price": "₹499", "image": "images/PsychologyOfMoney.jpg", "category": "Finance", "description": "Timeless lessons on wealth and happiness."},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "price": "₹399", "image": "images/ThinkAndGrowRich.jpg", "category": "Finance", "description": "Success through visualization and belief."},
    {"title": "The Millionaire Fastlane", "author": "MJ DeMarco", "price": "₹699", "image": "images/MillionaireFastlane.jpg", "category": "Finance", "description": "Crack the code to wealth and freedom."}
]

# --------- Layout ---------
left_spacer, main, right_panel = st.columns([0.1, 6, 2])

# --------- Routing ---------
if page == "Home":
    with main:
        st.title("✨ Welcome to Book Haven ✨")
        st.image("images/banner.jpg", width=500)
        st.markdown("### 🔥 Book Promotion")
        st.image("images/Spiderman.jpg", width=280, caption="🔥 Spiderman Comics!")
        st.markdown("---")
        st.markdown("## 📚 Categories")
        cols = st.columns(len(category_images))
        for i, (cat, img) in enumerate(category_images.items()):
            with cols[i]:
                st.image(img, width=80)
                st.caption(cat)
        st.markdown("---")
        st.subheader("🎭 Top Comics")
        for book in [b for b in books if b["category"] == "Comics"][:4]:
            st.image(book["image"], width=130)
            st.caption(book["title"])

    with right_panel:
        st.subheader("⭐ Top Rated")
        for title in ["Atomic Habits", "Harry Potter", "Design Patterns"]:
            for b in books:
                if b["title"] == title:
                    st.image(b["image"], width=100)
                    st.caption(b["title"])
        st.subheader("🆕 New Arrivals")
        for b in books[-4:]:
            st.image(b["image"], width=100)
            st.caption(b["title"])

elif page == "Books":
    with main:
        st.title("📚 Browse Books")
        selected_category = st.selectbox("Filter by Category", categories)
        display_books = [b for b in books if selected_category == "All" or b["category"] == selected_category]
        cols = st.columns(2)
        for i, book in enumerate(display_books):
            with cols[i % 2]:
                st.image(book["image"], width=200)
                st.markdown(f"**{book['title']}** by *{book['author']}*")
                st.write(f"💰 {book['price']}  |  🏷️ {book['category']}")
                st.caption(book["description"])
                if st.button(f"🛒 Add to Cart - {book['title']}", key=book['title']):
                    st.session_state.cart.append(book)
                    st.success(f"{book['title']} added to cart!")
                with st.expander("📝 Leave a Review"):
                    review = st.text_area(f"Write your review for {book['title']}", key=f"review_{book['title']}")
                    if st.button(f"Submit Review for {book['title']}", key=f"submit_{book['title']}"):
                        st.success(f"Thank you for reviewing {book['title']}!")

    with right_panel:
        st.subheader("💡 Recommended")
        for b in books[:3]:
            st.image(b["image"], width=100)
            st.caption(b["title"])

elif page == "Cart":
    with main:
        st.title("🛒 Your Cart")
        if st.session_state.cart:
            total = 0
            for item in st.session_state.cart:
                st.image(item["image"], width=100)
                st.write(f"**{item['title']}** - {item['price']}")
                total += int(item["price"].replace("₹", ""))
            st.subheader(f"Total: ₹{total}")
            if st.button("✅ Confirm Order"):
                st.session_state.order_history.append(st.session_state.cart.copy())
                st.success("✅ Order placed!")
                st.session_state.cart.clear()
        else:
            st.info("Your cart is empty.")

elif page == "Orders":
    with main:
        st.title("📦 Order History")
        if st.session_state.order_history:
            for i, order in enumerate(st.session_state.order_history[::-1], 1):
                st.subheader(f"🧾 Order #{i}")
                for item in order:
                    st.image(item["image"], width=100)
                    st.markdown(f"**{item['title']}** - {item['price']}")
        else:
            st.info("No past orders found.")

elif page == "Search":
    with main:
        st.title("🔎 Search Books")
        query = st.text_input("Enter title or author")
        if query:
            results = [b for b in books if query.lower() in b['title'].lower() or query.lower() in b['author'].lower()]
            if results:
                for book in results:
                    st.image(book["image"], width=120)
                    st.markdown(f"**{book['title']}** by *{book['author']}*")
                    st.write(f"💰 {book['price']} | 🏷️ {book['category']}")
            else:
                st.warning("No books found.")

elif page == "About":
    with main:
        st.title("📖 About Book Haven")

        st.markdown("""
        Welcome to **Book Haven** — a simple and friendly online bookstore made for everyone.

        We are based in **Thiruvarur** and offer a wide range of books, including:

        - 📘 Comics  
        - 📖 Fiction  
        - 💼 Finance  
        - 💻 Programming  
        - 🧘 Self Care

        Our goal is to make reading easy, fun, and affordable for all. Whether you're a student, a hobby reader, or just getting started, you’ll find something you love here.

        Thank you for visiting Book Haven! 😊
        """)

        st.image("images/logo.png", width=120)

elif page == "Contact":
    with main:
        st.title("✉️ Contact Us")
        st.write("We'd love to hear from you!")
        name = st.text_input("Your Name")
        message = st.text_area("Message")
        if st.button("Send Message"):
            st.success("Message sent! We'll get back to you soon.")
