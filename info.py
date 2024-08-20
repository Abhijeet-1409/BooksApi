from typing import List
from model import Book,Genre

books: List[Book] = [
    Book(
        book_title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        summary="A novel set in the 1920s that explores themes of wealth, class, and the American Dream.",
        description="The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald. It is set in the Jazz Age on Long Island, near New York City, and is narrated by Nick Carraway, who tells the story of Jay Gatsby and his unrequited love for Daisy Buchanan.",
        release_date="10-04-1925",
        publisher="Scribner",
        genre=Genre.FICTION
    ),
    Book(
        book_title="To Kill a Mockingbird",
        author="Harper Lee",
        summary="A novel about racial injustice and moral growth in the American South.",
        description="Published in 1960, To Kill a Mockingbird is a novel by Harper Lee. It is a classic of modern American literature and explores serious themes such as racial inequality and moral development through the eyes of young Scout Finch.",
        release_date="11-07-1960",
        publisher="J.B. Lippincott & Co.",
        genre=Genre.FICTION
    ),
    Book(
        book_title="1984",
        author="George Orwell",
        summary="A dystopian novel that examines the dangers of totalitarianism and extreme political ideology.",
        description="George Orwell's 1984 is a novel about a dystopian future where the government, led by Big Brother, exercises total control over every aspect of its citizens' lives. It serves as a powerful warning against the loss of personal freedoms.",
        release_date="08-06-1949",
        publisher="Secker & Warburg",
        genre=Genre.SCIENCE_FICTION
    ),
    Book(
        book_title="Pride and Prejudice",
        author="Jane Austen",
        summary="A romantic novel that critiques the British landed gentry at the end of the 18th century.",
        description="First published in 1813, Pride and Prejudice is one of Jane Austen's most famous novels. It follows the life of Elizabeth Bennet as she navigates issues of morality, upbringing, and marriage in the British gentry.",
        release_date="28-01-1813",
        publisher="T. Egerton",
        genre=Genre.ROMANCE
    ),
    Book(
        book_title="The Catcher in the Rye",
        author="J.D. Salinger",
        summary="A novel about teenage angst and alienation narrated by Holden Caulfield.",
        description="J.D. Salinger's The Catcher in the Rye, published in 1951, follows the experiences of Holden Caulfield, a disenchanted teenager who is struggling with issues of identity and belonging in post-World War II America.",
        release_date="16-07-1951",
        publisher="Little, Brown and Company",
        genre=Genre.DRAMA
    ),
    Book(
        book_title="The Hobbit",
        author="J.R.R. Tolkien",
        summary="A fantasy novel about the adventure of Bilbo Baggins.",
        description="Published in 1937, The Hobbit by J.R.R. Tolkien is a fantasy classic that tells the story of Bilbo Baggins' quest to help a group of dwarves reclaim their homeland from the dragon Smaug.",
        release_date="21-09-1937",
        publisher="George Allen & Unwin",
        genre=Genre.FANTASY
    ),
    Book(
        book_title="Moby Dick",
        author="Herman Melville",
        summary="A novel about the quest for revenge against the white whale, Moby Dick.",
        description="Herman Melville's Moby Dick, published in 1851, is an epic tale of Captain Ahab's obsessive quest to hunt down the titular whale. It explores themes of fate, revenge, and the human condition.",
        release_date="18-10-1851",
        publisher="Harper & Brothers",
        genre=Genre.ADVENTURE
    ),
    Book(
        book_title="Brave New World",
        author="Aldous Huxley",
        summary="A dystopian novel about a future society driven by technological advances and societal control.",
        description="Published in 1932, Aldous Huxley's Brave New World presents a futuristic society where technology and conditioning control human behavior and personal freedoms are sacrificed for stability and happiness.",
        release_date="01-09-1932",
        publisher="Chatto & Windus",
        genre=Genre.SCIENCE_FICTION
    ),
    Book(
        book_title="The Da Vinci Code",
        author="Dan Brown",
        summary="A thriller involving a murder in the Louvre and a secret society.",
        description="Dan Brown's The Da Vinci Code, published in 2003, is a fast-paced thriller that follows Robert Langdon as he uncovers secrets hidden in famous works of art and battles a secret society.",
        release_date="18-03-2003",
        publisher="Doubleday",
        genre=Genre.MYSTERY
    ),
    Book(
        book_title="The Shining",
        author="Stephen King",
        summary="A horror novel about a family staying in an isolated hotel with a dark history.",
        description="Published in 1977, Stephen King's The Shining tells the story of the Torrance family as they spend the winter at the Overlook Hotel, which harbors supernatural forces that drive the father to madness.",
        release_date="28-01-1977",
        publisher="Doubleday",
        genre=Genre.HORROR
    ),
    Book(
        book_title="Sapiens: A Brief History of Humankind",
        author="Yuval Noah Harari",
        summary="A non-fiction book that explores the history and impact of Homo sapiens on the world.",
        description="Yuval Noah Harari's Sapiens provides a sweeping history of the human species from the emergence of Homo sapiens to the present, examining how our species has shaped the world.",
        release_date="04-02-2011",
        publisher="Harvill Secker",
        genre=Genre.NON_FICTION
    )
]

# print("String representaion of book for user")
# for book in books :
#     print(str(book))

# print("\n")

# print("Detail representaion of book for developer")
# for book in books :
#     print(repr(book))