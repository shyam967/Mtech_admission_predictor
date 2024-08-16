document.getElementById('admissionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const gre = parseInt(document.getElementById('gre').value);
    const toefl = parseInt(document.getElementById('toefl').value);
    const rating = parseInt(document.getElementById('rating').value);
    const sop = parseFloat(document.getElementById('sop').value);
    const lor = parseFloat(document.getElementById('lor').value);
    const cgpa = parseFloat(document.getElementById('cgpa').value);
    const research = parseInt(document.getElementById('research').value);

    // Example prediction logic (this should be replaced with actual model or API call)
    let predictedChance = Math.min(100, ((gre + toefl + rating * 100 + sop * 100 + lor * 100 + cgpa * 10 + research * 100) / 2000) * 100);

    // Display prediction
    document.getElementById('predictedChance').innerText = predictedChance.toFixed(2) + '%';

    // Example recommended universities (this should be replaced with actual data filtering logic)
    let recommendedUniversities = ['University A', 'University B', 'University C'];
    let list = document.getElementById('universityList');
    list.innerHTML = '';
    recommendedUniversities.forEach(function(university) {
        let li = document.createElement('li');
        li.innerText = university;
        list.appendChild(li);
    });
});

