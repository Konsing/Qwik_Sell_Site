import React, { useState, useEffect } from 'react';
import './FeaturedCarousel.css';

const featuredProducts = [
  {
    id: 1,
    name: "Gaming PC",
    image: "/images/product1.png",
    description: "High performance gaming PC for the ultimate gaming experience."
  },
  {
    id: 2,
    name: "Ultra HD Monitor",
    image: "/images/product2.png",
    description: "Stunning visuals with our ultra HD monitors."
  },
  {
    id: 3,
    name: "RGB Mechanical Keyboard",
    image: "/images/product3.png",
    description: "Enhance your gaming setup with our RGB mechanical keyboards."
  },
];

function FeaturedCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const totalSlides = featuredProducts.length;

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex(prev => (prev + 1) % totalSlides);
    }, 5000);
    return () => clearInterval(timer);
  }, [totalSlides]);

  const goToPrevious = () => {
    setCurrentIndex((currentIndex - 1 + totalSlides) % totalSlides);
  };

  const goToNext = () => {
    setCurrentIndex((currentIndex + 1) % totalSlides);
  };

  return (
    <section className="carousel" aria-label="Featured Products Carousel">
      <img 
        src={featuredProducts[currentIndex].image} 
        alt={featuredProducts[currentIndex].name} 
        className="carousel-image" 
      />
      <div className="carousel-caption">
        <h2>{featuredProducts[currentIndex].name}</h2>
        <p>{featuredProducts[currentIndex].description}</p>
      </div>
      <button className="carousel-control prev" onClick={goToPrevious} aria-label="Previous Slide">&#10094;</button>
      <button className="carousel-control next" onClick={goToNext} aria-label="Next Slide">&#10095;</button>
      <div className="carousel-indicators">
        {featuredProducts.map((_, idx) => (
          <button 
            key={idx} 
            className={`indicator ${idx === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(idx)}
            aria-label={`Slide ${idx + 1}`}
          />
        ))}
      </div>
    </section>
  );
}

export default FeaturedCarousel;
