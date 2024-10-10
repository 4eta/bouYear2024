import React from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const useLogin = () => {
  const navigate = useNavigate();

  const login = (user) => {
    console.log("ログイン処理");
    // ユーザーの存在確認と登録のエンドポイント
    const endpoint = "http://127.0.0.1:8000/users";  

    // クエリにfirst_name, last_name, affiliationを使用
    const queries = { 
      first_name: user.first_name, 
      last_name: user.last_name, 
      affiliation: user.affiliation 
    };

    // ユーザーの存在確認
    axios
      .get(endpoint, { params: queries })
      .then((res) => {
        console.log(res.data);

        // ユーザーが存在する場合
        if (Object.keys(res.data).length > 0) {
          console.log("ユーザーが既に存在しています。ログインします。");
          // ユーザー情報をlocalStorageに保存
          localStorage.setItem("loginUser", JSON.stringify({
            first_name: user.first_name,
            last_name: user.last_name,
            affiliation: user.affiliation
          }));
          localStorage.setItem("isLogined", "true");

          // ホーム画面にリダイレクト
          navigate("/", { state: { username: `${user.first_name} ${user.last_name}` } });

        } else {
          // ユーザーが存在しない場合、新規登録処理
          console.log("ユーザーが存在しません。新規登録します。");

          // 新規登録APIへのPOSTリクエスト
          axios
            .post(endpoint, queries)  
            .then((res) => {
              console.log("新規登録成功。ログインします。");
              // ユーザー情報をlocalStorageに保存
              localStorage.setItem("loginUser", JSON.stringify({
                first_name: user.first_name,
                last_name: user.last_name,
                affiliation: user.affiliation
              }));
              localStorage.setItem("isLogined", "true");

              // ホーム画面にリダイレクト
              navigate("/", { state: { username: `${user.first_name} ${user.last_name}` } });
            })
            .catch((err) => {
              console.log("新規登録に失敗しました。", err);
              localStorage.removeItem("loginUser");
              localStorage.setItem("isLogined", "false");
              navigate("/loginfailed");
            });
        }
      })
      .catch((err) => {
        console.log("ログインに失敗しました。", err);
        localStorage.removeItem("loginUser");
        localStorage.setItem("isLogined", "false");
        navigate("/loginfailed");
      });
  };

  return { login };
};
