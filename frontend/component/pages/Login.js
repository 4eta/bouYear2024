import React, { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import '../css/common.css';
import '../css/login.css';

const Login = () => {
  const [lastName, setLastName] = useState('');
  const [firstName, setFirstName] = useState('');
  const [department, setDepartment] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // 入力データを処理するロジックをここに追加
    console.log(`苗字: ${lastName}, 名前: ${firstName}, 所属: ${department}`);
  };

  return (
    <div className="background">
      <div className="blur">
        <form onSubmit={handleSubmit}>
          <div className="subtitle">
            <p>オンリーワンゲーム</p>
            <p>の参加ページです。</p>
          </div>
          <div>
            <label>苗字:</label>
            <input
              type="text"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
          </div>
          <div>
            <label>名前:</label>
            <input
              type="text"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
          </div>
          <TextField id="outlined-basic" label="Outlined" variant="outlined" sx={{
        '& .MuiOutlinedInput-root': {
          backgroundColor: 'white',
        },
      }}/>
          <div>
            <label>所属:</label>
            <select
              value={department}
              onChange={(e) => setDepartment(e.target.value)}
            >
              <option value="">選択してください</option>
              <option value="IM">IM</option>
              <option value="AMB">AMB</option>
              <option value="HA">HA</option>
            </select>
          </div>
          <button type="submit">入室</button>
          <Button variant="contained">Contained</Button>
        </form>
      </div>
    </div>
  );
};

export default Login;
