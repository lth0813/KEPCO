import './App.css';
import {BrowserRouter, Routes, Route, NavLink, Outlet, useParams} from 'react-router-dom'

const contents = [
  {id : 1, title : "HTML", desc : "HTML is for information"},
  {id : 2, title : "JS", desc : "JavaScript is for interactive"},
  {id : 3, title : "React", desc : "React is for fun"},
]

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home....
    </div>
  );
}

function Topics() {
  const lists = [];
  for (let i = 0; i < contents.length; i++) {
    lists.push(
      <li key={contents[i].id}>
        <NavLink to={`/topics/${contents[i].id}`}>{contents[i].title}</NavLink>
      </li>
    )
  }
  return (
    <div>
      <h2>Topics</h2>
      Topics....
      <ul>
        {lists}
      </ul>

      <Outlet></Outlet>
    </div>
  );
}

function Topic() {
  const {id} = useParams();
  let selected_topic = {
    title:"Sorry",
    desc:"Not Found"
  }
  for (const topic of contents) {
    if(topic.id === Number(id)) {
      selected_topic = topic;
      break;
    }
  }
  return(
    <div>
      <h3>{selected_topic.title}</h3>
      <h5>{selected_topic.desc}</h5>
    </div>
  )
}

function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact....
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <div className='App'>
        <h1>React Router DOM Example</h1>
        <ul>
          <li><NavLink to="/">Home</NavLink></li>
          <li><NavLink to="/topics">Topics</NavLink></li>
          <li><NavLink to="/contact">Contact</NavLink></li>
        </ul>
        <Routes>
          <Route path='/' element={<Home/>}></Route>
          <Route path='/topics' element={<Topics/>}>
            <Route path=':id' element={<Topic/>}></Route>
          </Route>
          <Route path='/contact' element={<Contact/>}></Route>
          
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;
