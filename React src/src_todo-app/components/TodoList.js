import TodoListItem from './TodoListItem';
import '../css/TodoList.css';

const TodoList = (props) => {
    const lists = [];
    for(let i = 0; i < props.todos.length; i++) {
        lists.push(
            <TodoListItem todo={props.todos[i]} key={props.todos[i].id} onRemove={props.onRemove} onToggle={props.onToggle}/>
        );
    }
    return ( 
        <div className='TodoList'>
            { lists }
        </div>
    );
};

export default TodoList;