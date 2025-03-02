import React from 'react';
import { useParams } from 'react-router-dom';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/ProductsPage.css';

const dummyProducts = {
  1: {
    id: 1,
    name: "Gaming PC",
    image: "/images/product1.png",
    description: "Experience ultimate performance with our state-of-the-art Gaming PC.",
    price: "$1499",
    specs: {
      CPU: "Intel i7",
      GPU: "NVIDIA RTX 3070",
      RAM: "16GB",
      Storage: "1TB SSD"
    }
  },
  // Additional dummy products can be added here
};

function ProductsPage() {
  const { id } = useParams();
  const product = dummyProducts[id] || {
    id: 0,
    name: "Product Not Found",
    image: "/images/placeholder.png",
    description: "We couldn't find the product you are looking for.",
    price: "",
    specs: {}
  };

  return (
    <div>
      <Header />
      <main className="product-page">
        <div className="product-details">
          <img src={product.image} alt={product.name} className="product-image" />
          <div className="details">
            <h2 className="product-name">{product.name}</h2>
            <p className="product-description">{product.description}</p>
            {product.price && <p className="product-price">Price: {product.price}</p>}
            {product.specs && Object.keys(product.specs).length > 0 && (
              <div className="product-specs">
                <h3>Specifications:</h3>
                <ul>
                  {Object.entries(product.specs).map(([key, value]) => (
                    <li key={key}><strong>{key}:</strong> {value}</li>
                  ))}
                </ul>
              </div>
            )}
            <button className="add-to-cart-btn">Add to Cart</button>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default ProductsPage;
