import React, { useEffect } from 'react';
import axios from 'axios';

function App() {
  useEffect(() => {
    // Realizamos la solicitud GET al endpoint de Django
    axios.get('http://localhost:8000/api/test/')
      .then(response => {
        console.log(response.data);  // Deberías ver {"message": "OK"}
      })
      .catch(error => {
        console.error('Error al hacer la solicitud:', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>¡Prueba de conexión con Django y React!</h1>
    </div>
  );
}

export default App;
