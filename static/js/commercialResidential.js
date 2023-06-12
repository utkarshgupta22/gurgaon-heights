const mainCarousel = document.querySelector('.carousel-main');
    const thumbnailCarousel = document.querySelector('.carousel-thumbnails');
    const mainCarouselItems = document.querySelectorAll('.carousel-item');
    const thumbnailCarouselItems = document.querySelectorAll('.carousel-thumbnail');
    
    thumbnailCarousel.addEventListener('click', (e) => {
      const thumbnailClicked = e.target.closest('.carousel-thumbnail');
      if (!thumbnailClicked) return;
      const thumbnailIndex = [...thumbnailCarouselItems].indexOf(thumbnailClicked);
    
      mainCarouselItems.forEach((item) => {
        item.classList.remove('active');
      });
      thumbnailCarouselItems.forEach((item) => {
        item.classList.remove('active');
      });
    
      mainCarouselItems[thumbnailIndex].classList.add('active');
      thumbnailCarouselItems[thumbnailIndex].classList.add('active');
    });