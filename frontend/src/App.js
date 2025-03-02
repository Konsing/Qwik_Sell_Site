import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ProductPage from './pages/ProductsPage';
import CartPage from './pages/CartPage';
import NotFoundPage from './pages/NotFoundPage';
import './Styles/Global.css';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/product/:id" element={<ProductPage />} />
        <Route path="/cart" element={<CartPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
}

export default App;
