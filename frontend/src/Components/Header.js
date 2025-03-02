import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';

function Header() {
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchTerm.trim() !== '') {
      navigate(`/search?query=${encodeURIComponent(searchTerm)}`);
    }
  };

  return (
    <header className="header">
      <div className="header-left">
        <Link to="/"><h1 className="logo">CircuitCart</h1></Link>
      </div>
      <div className="header-center">
        <form className="search-form" onSubmit={handleSearchSubmit}>
          <input 
            type="text" 
            placeholder="Search products..." 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            aria-label="Search products"
          />
          <button type="submit" aria-label="Search">🔍</button>
        </form>
      </div>
      <div className="header-right">
        <nav className="nav-menu">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/products">Products</Link></li>
            <li><Link to="/cart">Cart</Link></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
