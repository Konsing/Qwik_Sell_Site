import React, { useRef } from 'react';
import ProductCard from './ProductCard';
import './ProductRow.css';

function ProductRow({ title, products }) {
  const containerRef = useRef(null);
  const scrollStep = 10 * 90; // Assuming each card is ~90px wide (80px width + 10px gap)

  const scrollLeft = () => {
    if (containerRef.current) {
      containerRef.current.scrollBy({
        left: -scrollStep,
        behavior: 'smooth',
      });
    }
  };

  const scrollRight = () => {
    if (containerRef.current) {
      containerRef.current.scrollBy({
        left: scrollStep,
        behavior: 'smooth',
      });
    }
  };

  return (
    <div className="product-row">
      <div className="row-header">
        <h2 className="row-title">{title}</h2>
      </div>
      <div className="product-row-wrapper">
        <button className="scroll-btn left" onClick={scrollLeft} aria-label="Scroll Left">
          &#10094;
        </button>
        <div className="row-products" ref={containerRef}>
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
        <button className="scroll-btn right" onClick={scrollRight} aria-label="Scroll Right">
          &#10095;
        </button>
      </div>
    </div>
  );
}

export default ProductRow;
