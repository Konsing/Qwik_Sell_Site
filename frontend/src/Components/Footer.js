import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-links">
        <a href="/about">About Us</a>
        <a href="/support">Support</a>
        <a href="/contact">Contact</a>
        <a href="/terms">Terms of Service</a>
      </div>
      <div className="footer-social">
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a>
      </div>
      <p>&copy; {new Date().getFullYear()} CircuitCart. All rights reserved.</p>
    </footer>
  );
}

export default Footer;
