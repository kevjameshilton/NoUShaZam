// import React, { Fragment } from 'react'

// export const Input = () => {
//     const onSubmit = e => {
//         e.preventDefault();
//         if (text === "") {
//           alertContext.setAlert("Please enter something", "light");
//         } else {
//           githubContext.searchUsers(text);
//           setText("");
//         }
//       };

//     return (
//         <Fragment>
//         <form onSubmit={onSubmit} className="form">
//         <input
//           type="text"
//           name="text"
//           placeholder="Search Users..."
//           value={text}
//           onChange={onChange}
//         />
//         <input
//           type="submit"
//           value="Search"
//           className="btn btn-dark btn-block"
//         />
//       </form>
//       {githubContext.users.length > 0 && (
//         <button
//           className="btn btn-light btn-block"
//           onClick={githubContext.clearUsers}
//         >
//           Clear
//         </button>
//       )}
//         </Fragment>
//     )
// }

// export default Search;

// const Search = () => {
//   const githubContext = useContext(GithubContext);
//   const alertContext = useContext(AlertContext);

//   const [text, setText] = useState("");

//   const onChange = e => setText(e.target.value);

//   return (
//     <div>

//     </div>
//   );
// };

// export default Search;
