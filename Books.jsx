import { useEffect, useState } from "react";
import axios from "axios";

function Books() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get(
      "http://library.local:8000/api/resource/Book?fields=[\"name\",\"book_title\",\"author\",\"isbn\",\"available_copies\"]",
      { withCredentials: true }
    )
    .then(res => {
      setBooks(res.data.data);
    })
    .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Library Books</h1>

      {books.map((book) => (
        <div key={book.name} style={{border: "1px solid gray", margin: "10px", padding: "10px"}}>
          <h3>{book.book_title}</h3>
          <p>Author: {book.author}</p>
          <p>ISBN: {book.isbn}</p>
          <p>Available: {book.available_copies}</p>
        </div>
      ))}
    </div>
  );
}

export default Books;