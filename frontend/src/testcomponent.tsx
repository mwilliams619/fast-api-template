import React, { useState, useEffect } from 'react';

const TestComponent = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('/');
      const data = await response.json();
      setMessage(data.message);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
};

export default TestComponent;