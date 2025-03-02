import React from 'react';
import { Link } from 'react-router-dom';
import './ProductCard.css';

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <Link to={`/product/${product.id}`}>
        <img 
          src={product.image} 
          alt={product.name} 
          className="product-image" 
        />
        <div className="product-info">
          <h3 className="product-name">{product.name}</h3>
        </div>
      </Link>
    </div>
  );
}

export default ProductCard;
