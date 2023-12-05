import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MyComponent = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8080/api/data')
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div>
            여기는 프론트엔드에서 온 데이터입니다.<br/>
            이쪽은 {data}
        </div>
    );
};

export default MyComponent;