PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Biographies', 'biographies-category.jpg'),
(2, 'Learn to Play', 'learn-to-play-category.jpg'),
(3, 'Music Theory', 'music-theory-category.jpg'),
(4, 'Scores and Collections', 'scores-and-collections-category.jpg'),
(5, 'Autobiographies', 'autobiographies-category.jpg'),
(6, 'Science Fiction', 'science-fiction-category.jpg'),
(7, 'Romantic Comedy', 'romantic-comedy-category.jpg'),
(8, 'Horror', 'horror-category.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Beethoven: Anguish and Triumph', 'Jan Swafford', '9780618054749', 24.99, 'beethoven.gif', 1),
(2, 1, 'Lady Gaga: Applause', 'Annie Zaleski', '9781250203564', 19.99, 'madonna.jpg', 0),
(3, 1, 'Duke: A Life of Duke Ellington', 'Terry Teachout', '9781594036682', 21.99, 'ellington.jpg', 0),
(4, 1, 'Clapton: The Autobiography', 'Eric Clapton', '9780767920551', 18.99, 'clapton.jpg', 0),
(5, 2, 'Hal Leonard Guitar Method Book 1', 'Will Schmid', '9780793523054', 14.99, 'guitar.jpg', 1),
(6, 2, 'Alfred''s Basic Adult Piano Course Lesson Book 1', 'Willard A. Palmer', '9780882846163', 16.99, 'piano.jpg', 1),
(7, 3, 'Music Theory for Dummies', 'Michael Pilhofer', '9781119575528', 22.99, 'theory.jpg', 1),
(8, 4, 'The Real Book: Volume I (C Edition)', 'Hal Leonard Corp.', '9780634060380', 39.99, 'scores.jpg', 0),
(9, 5, 'The Diary of a Young Girl', 'Anne Frank', '9780385480338', 11.99, 'diary-of-a-young-girl.jpg', 1),
(10, 5, 'I Am Malala (Young Readers Edition)', 'Malala Yousafzai', '9780316327916', 10.99, 'i-am-malala.jpg', 1),
(11, 5, 'Becoming', 'Michelle Obama', '9781524763145', 20.00, 'becoming.jpg', 0),
(12, 6, 'Project Hail Mary', 'Andy Weir', '9780593135228', 22.00, 'project-hail-mary.jpg', 1),
(13, 6, 'Dune', 'Frank Herbert', '9780441013593', 20.00, 'dune.jpg', 0),
(14, 6, '1984', 'George Orwell', '9780451524935', 19.00, '1984.jpg', 1),
(15, 7, 'The Hating Game', 'Sally Thorne', '9780062439598', 15.99, 'the-hating-game.jpg', 0),
(16, 7, 'Funny Story', 'Emily Henry', '9780593441213', 19.00, 'funny-story.jpg', 1),
(17, 7, 'The Love Hypothesis', 'Ali Hazelwood', '9780593336823', 16.00, 'the-love-hypothesis.jpg', 0),
(18, 8, 'Dracula', 'Bram Stoker', '9781435159570', 15.00, 'dracula.jpg', 1),
(19, 8, 'Misery', 'Stephen King', '9781668094709', 19.99, 'misery.jpg', 0),
(20, 8, 'Frankenstein', 'Mary Shelley', '9780141439471', 12.00, 'frankenstein.jpg', 1);

