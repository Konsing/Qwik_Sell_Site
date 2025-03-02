import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/NotFoundPage.css';

function NotFoundPage() {
  return (
    <div className="not-found-page">
      <Header />
      <main className="not-found-content">
        <h2>404 - Page Not Found</h2>
        <p>The page you are looking for does not exist.</p>
        <Link to="/" className="home-link">Return Home</Link>
      </main>
      <Footer />
    </div>
  );
}

export default NotFoundPage;
