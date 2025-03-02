import React from 'react';
import Header from '../Components/Header';
import FeaturedCarousel from '../Components/FeaturedCarousel';
import ProductRow from '../Components/ProductRow';
import Footer from '../Components/Footer';
import '../Styles/HomePage.css';

function HomePage() {
  // Dummy product data for different categories
  const dealsProducts = [
    { id: 1, name: "Discounted CPU", image: "/images/prod1.png" },
    { id: 2, name: "Budget Motherboard", image: "/images/prod2.png" },
    { id: 3, name: "Affordable RAM", image: "/images/prod3.png" },
    { id: 4, name: "Cheap SSD", image: "/images/prod4.png" },
    { id: 5, name: "Discounted GPU", image: "/images/prod5.png" },
    { id: 6, name: "Budget Power Supply", image: "/images/prod6.png" },
    { id: 7, name: "Affordable Case", image: "/images/prod7.png" },
    { id: 8, name: "Cheap Cooler", image: "/images/prod8.png" },
  ];

  const newestArrivals = [
    { id: 9, name: "Latest GPU", image: "/images/prod9.png" },
    { id: 10, name: "New CPU", image: "/images/prod10.png" },
    { id: 11, name: "Next-gen Motherboard", image: "/images/prod11.png" },
    { id: 12, name: "Advanced Cooling", image: "/images/prod12.png" },
    { id: 13, name: "New RAM", image: "/images/prod13.png" },
    { id: 14, name: "Next-gen SSD", image: "/images/prod14.png" },
    { id: 15, name: "Latest Case", image: "/images/prod15.png" },
    { id: 16, name: "New Power Supply", image: "/images/prod16.png" },
  ];

  const topRated = [
    { id: 17, name: "NVIDIA RTX 3080", image: "/images/prod17.png" },
    { id: 18, name: "AMD Radeon RX 6800", image: "/images/prod18.png" },
    { id: 19, name: "NVIDIA GTX 1660", image: "/images/prod19.png" },
    { id: 20, name: "AMD Radeon RX 5700", image: "/images/prod20.png" },
    { id: 21, name: "NVIDIA RTX 3070", image: "/images/prod21.png" },
    { id: 22, name: "AMD Radeon RX 6700", image: "/images/prod22.png" },
    { id: 23, name: "NVIDIA GTX 1650", image: "/images/prod23.png" },
    { id: 24, name: "AMD Radeon RX 5600", image: "/images/prod24.png" },
  ];

  return (
    <div>
      <Header />
      <main className="home-page">
        <FeaturedCarousel />
        <ProductRow title="Deals" products={dealsProducts} />
        <ProductRow title="Newest Arrivals" products={newestArrivals} />
        <ProductRow title="Top Rated" products={topRated} />
      </main>
      <Footer />
    </div>
  );
}

export default HomePage;
