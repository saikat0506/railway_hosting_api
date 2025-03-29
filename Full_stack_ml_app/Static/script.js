async function predict() {
    const feature1 = document.getElementById("feature1").value;
    const feature2 = document.getElementById("feature2").value;
    const feature3 = document.getElementById("feature3").value;
    const feature4 = document.getElementById("feature4").value;

    const inputData = { feature1: parseFloat(feature1), feature2: parseFloat(feature2), feature3: parseFloat(feature3), feature4: parseFloat(feature4) };

    try {
        const response = await fetch("/predict/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(inputData)
        });

        const result = await response.json();
        document.getElementById("result").innerHTML = "Prediction: " + result.prediction[0];

    } catch (error) {
        document.getElementById("result").innerHTML = "Error: Unable to connect to API.";
    }
}