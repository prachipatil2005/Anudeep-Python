// // Smooth Scroll for Menu Links
document.querySelectorAll('.menu li a').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        window.scrollTo({
          top: target.offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // Hover Animation for Cards
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseover', () => {
      card.style.transform = 'translateY(-15px) scale(1.1)';
      card.style.transition = '0.4s';
    });
    card.addEventListener('mouseout', () => {
      card.style.transform = 'translateY(0) scale(1)';
    });
  });
  