import { Component, useState } from 'react';
import './App.css';

class ClassComp extends Component {
  state = {
    number:this.props.initNumber,
    date: new Date().toString()
  }
  render() {
    return (
      <div className="container">
        <h2>Class Style Component</h2>
        <p>Number : {this.state.number}</p>
        <button type='button' onClick={() => {
          this.setState({number: parseInt(Math.random()*10)})
        }}>Random 선택</button>
        <p>Date : {this.state.date}</p>
        <button type='button' onClick={() => {
          this.setState({date: new Date().toString()});
        }}>Date</button>
      </div>
    )
  }
}

function FunctionComp(props) {
  const numberState = useState(props.initNumber);
  const number = numberState[0];
  const setNumber = numberState[1];
  const dateState = useState(new Date().toString());
  const date = dateState[0];
  const setDate = dateState[1];
  return (
    <div className="container">
      <h2>Function Style Component</h2>
      <p>Number : { number }</p>
      <button type="button" onClick={ () => {setNumber(parseInt(Math.random()*10)); setDate(new Date().toString());}}>Random 선택</button>
      <p>Date : { date }</p>
    </div>
  )
}

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>
      <ClassComp initNumber={1}/>
      <FunctionComp initNumber={1}/>
    </div>
  );
}

export default App;
