const { useEffect, useMemo, useState } = React;

const API_BASE_URL = window.API_BASE_URL || "http://127.0.0.1:8000";
const BOOKS_URL = `${API_BASE_URL}/books`;
const LOGIN_URL = `${API_BASE_URL}/login`;
const BOOK_TYPE_LABELS = {
    physical: "Physical Book",
    ebook: "EBook",
};

function BookCard({ book, isFavorite, onToggleFavorite }) {
    const bookTypeLabel = BOOK_TYPE_LABELS[book.book_type] || "Book";

    return (
        <article className="book-card">
            <div className="cover-placeholder">{bookTypeLabel}</div>
            <div className="book-body">
                <h2 className="book-title">{book.title}</h2>
                <p className="book-author">by {book.author}</p>
                <p className="book-meta">Published: {book.year}</p>
                <p className="book-meta">Extra info: {book.extra_info}</p>
                <button
                    type="button"
                    className={`favorite-button ${isFavorite ? "is-favorite" : ""}`}
                    onClick={() => onToggleFavorite(book.id)}
                >
                    {isFavorite ? "♥ Favorited" : "♡ Add to favorites"}
                </button>
            </div>
        </article>
    );
}

function App() {
    const [books, setBooks] = useState([]);
    const [favorites, setFavorites] = useState({});
    const [searchQuery, setSearchQuery] = useState("");
    const [authorQuery, setAuthorQuery] = useState("");
    const [isLoading, setIsLoading] = useState(true);
    const [errorMessage, setErrorMessage] = useState("");
    const [loginForm, setLoginForm] = useState({ username: "", password: "" });
    const [bookForm, setBookForm] = useState({
        title: "",
        author: "",
        year: "",
        book_type: "physical",
        extra_info: "",
    });
    const [token, setToken] = useState("");
    const [authMessage, setAuthMessage] = useState("");
    const [formMessage, setFormMessage] = useState("");
    const [isSubmittingBook, setIsSubmittingBook] = useState(false);

    async function loadBooks(author = "") {
        setIsLoading(true);
        setErrorMessage("");

        try {
            const url = author
                ? `${BOOKS_URL}?author=${encodeURIComponent(author)}`
                : BOOKS_URL;

            const response = await fetch(url);

            if (!response.ok) {
                throw new Error("Could not load books from the API.");
            }

            const apiBooks = await response.json();
            setBooks(apiBooks);
        } catch (error) {
            setErrorMessage(error.message);
        } finally {
            setIsLoading(false);
        }
    }

    useEffect(() => {
        loadBooks();
    }, []);

    function handleLoginFieldChange(event) {
        const { name, value } = event.target;
        setLoginForm((currentForm) => ({
            ...currentForm,
            [name]: value,
        }));
    }

    function handleBookFieldChange(event) {
        const { name, value } = event.target;
        setBookForm((currentForm) => ({
            ...currentForm,
            [name]: value,
        }));
    }

    function handleAuthorSearch(event) {
        event.preventDefault();
        loadBooks(authorQuery);
    }

    async function handleLogin(event) {
        event.preventDefault();
        setAuthMessage("");

        try {
            const response = await fetch(LOGIN_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(loginForm),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Login failed.");
            }

            setToken(data.access_token);
            setAuthMessage("Login successful. Authenticated actions are now enabled.");
        } catch (error) {
            setToken("");
            setAuthMessage(error.message);
        }
    }

    function handleLogout() {
        setToken("");
        setAuthMessage("You have been logged out.");
    }

    async function handleAddBook(event) {
        event.preventDefault();

        if (!token) {
            setFormMessage("Please log in before adding a book.");
            return;
        }

        setIsSubmittingBook(true);
        setFormMessage("");

        try {
            const response = await fetch(BOOKS_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({
                    ...bookForm,
                    year: Number(bookForm.year),
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Could not add book.");
            }

            setFormMessage(`Book added successfully with id ${data.id}.`);
            setBookForm({
                title: "",
                author: "",
                year: "",
                book_type: "physical",
                extra_info: "",
            });
            await loadBooks();
        } catch (error) {
            setFormMessage(error.message);
        } finally {
            setIsSubmittingBook(false);
        }
    }

    function handleToggleFavorite(bookId) {
        setFavorites((currentFavorites) => ({
            ...currentFavorites,
            [bookId]: !currentFavorites[bookId],
        }));
    }

    const filteredBooks = useMemo(() => {
        const normalizedQuery = searchQuery.trim().toLowerCase();

        if (!normalizedQuery) {
            return books;
        }

        return books.filter((book) =>
            book.title.toLowerCase().includes(normalizedQuery)
        );
    }, [books, searchQuery]);

    return (
        <div className="page-shell">
            <header className="page-header">
                <h1>React Book Catalog</h1>
                <p>Live book data from the Day 7 API with login, favorites, and authenticated book creation.</p>
                <p className="api-hint">API base URL: {API_BASE_URL}</p>
                <input
                    className="search-input"
                    type="text"
                    placeholder="Search books by title"
                    value={searchQuery}
                    onChange={(event) => setSearchQuery(event.target.value)}
                />
                <form className="stacked-form" onSubmit={handleAuthorSearch}>
                    <label>
                        Search books by author
                        <input
                            className="search-input"
                            type="text"
                            placeholder="Enter author name"
                            value={authorQuery}
                            onChange={(event) => setAuthorQuery(event.target.value)}
                        />
                    </label>
                    <div className="button-row">
                        <button type="submit" className="action-button">Search Author</button>
                        <button
                            type="button"
                            className="ghost-button"
                            onClick={() => {
                                setAuthorQuery("");
                                loadBooks();
                            }}
                        >
                            Reset
                        </button>
                    </div>
                </form>
            </header>

            <main className="catalog-content">
                <section className="control-panel">
                    <article className="panel-card">
                        <h2>Login</h2>
                        <form className="stacked-form" onSubmit={handleLogin}>
                            <label>
                                Username
                                <input
                                    type="text"
                                    name="username"
                                    value={loginForm.username}
                                    onChange={handleLoginFieldChange}
                                />
                            </label>
                            <label>
                                Password
                                <input
                                    type="password"
                                    name="password"
                                    value={loginForm.password}
                                    onChange={handleLoginFieldChange}
                                />
                            </label>
                            <div className="button-row">
                                <button type="submit" className="action-button">Log in</button>
                                <button type="button" className="ghost-button" onClick={handleLogout}>Log out</button>
                            </div>
                        </form>
                        <p className="panel-message">{token ? "Authenticated" : "Not authenticated"}</p>
                        {authMessage && <p className="panel-message">{authMessage}</p>}
                    </article>

                    <article className="panel-card">
                        <h2>Add Book</h2>
                        <form className="stacked-form" onSubmit={handleAddBook}>
                            <label>
                                Title
                                <input
                                    type="text"
                                    name="title"
                                    value={bookForm.title}
                                    onChange={handleBookFieldChange}
                                    required
                                />
                            </label>
                            <label>
                                Author
                                <input
                                    type="text"
                                    name="author"
                                    value={bookForm.author}
                                    onChange={handleBookFieldChange}
                                    required
                                />
                            </label>
                            <label>
                                Year
                                <input
                                    type="number"
                                    name="year"
                                    value={bookForm.year}
                                    onChange={handleBookFieldChange}
                                    min="1"
                                    required
                                />
                            </label>
                            <label>
                                Book Type
                                <select
                                    name="book_type"
                                    value={bookForm.book_type}
                                    onChange={handleBookFieldChange}
                                >
                                    <option value="physical">Physical</option>
                                    <option value="ebook">EBook</option>
                                </select>
                            </label>
                            <label>
                                Extra Info
                                <input
                                    type="text"
                                    name="extra_info"
                                    value={bookForm.extra_info}
                                    onChange={handleBookFieldChange}
                                    required
                                />
                            </label>
                            <button type="submit" className="action-button" disabled={isSubmittingBook}>
                                {isSubmittingBook ? "Adding..." : "Add Book"}
                            </button>
                        </form>
                        {formMessage && <p className="panel-message">{formMessage}</p>}
                    </article>
                </section>

                {isLoading && <div className="status-message">Loading books...</div>}
                {!isLoading && errorMessage && (
                    <div className="status-message">{errorMessage}</div>
                )}
                {!isLoading && !errorMessage && filteredBooks.length === 0 && (
                    <div className="status-message">No books match your search.</div>
                )}
                {!isLoading && !errorMessage && filteredBooks.length > 0 && (
                    <section className="book-grid">
                        {filteredBooks.map((book) => (
                            <BookCard
                                key={book.id}
                                book={book}
                                isFavorite={Boolean(favorites[book.id])}
                                onToggleFavorite={handleToggleFavorite}
                            />
                        ))}
                    </section>
                )}
            </main>

            <footer className="page-footer">
                <p>Day 14 Frontend Framework Intro - React Book Catalog</p>
            </footer>
        </div>
    );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);