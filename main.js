// main.js

// This file will handle the interactivity of the website

document.addEventListener('DOMContentLoaded', () => {
    // Get all the navigation links
    const navLinks = document.querySelectorAll('nav ul li a');

    // Add click event listener to each link
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();

            // Get the section to scroll to
            const targetSection = document.querySelector(event.target.getAttribute('href'));

            // Scroll to the section
            targetSection.scrollIntoView({behavior: 'smooth'});
        });
    });
});
