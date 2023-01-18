import './App.css';
import { Route, Routes } from 'react-router-dom';
import UploadImage from './views/UploadImage';

function App(): JSX.Element {
  return (
    <Routes>
      <Route path="/" element={<UploadImage />} />
    </Routes>
  );
}

export default App;
