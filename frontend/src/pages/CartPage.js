import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/CartPage.css';

function CartPage() {
  // For demonstration, assume the cart is empty.
  return (
    <div className="cart-page">
      <Header />
      <main className="cart-content">
        <h2>Your Cart</h2>
        <p>No items in your cart yet.</p>
      </main>
      <Footer />
    </div>
  );
}

export default CartPage;
