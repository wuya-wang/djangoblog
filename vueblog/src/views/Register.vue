<template>
  <div class="register" :style="{ height: bodyHeight + 'px' }">
    <div class="register-main">
      <div class="navbar">
        <div class="navbar-register" @click="goRegister()">
          <i class="iconfont icon-zhuce"></i>
          <p>REGISTER</p>
        </div>
        <div class="navbar-login" @click="goLogin()">
          <i class="iconfont icon-zhiwendenglu"></i>
          <p>LOGIN</p>
        </div>
      </div>
      <el-row>
        <el-col :xs="20" :sm="16" :md="10" :lg="6" :xl="6" :style="{top: Top + 'px'}">
          <div class="login-box">
            <el-card class="box-card">
              <div slot="header" class="clearfix login__card_title">
                <span>REGISTER</span>
              </div>
              <div class="form" v-show="Register">
                 <div class="input" :class="{'focus':focusEmail}" placeholder="Email">
                  <el-input @focus="inEmail()" @blur="outEmail()" v-model="userinfo.email" type="text"></el-input>
                </div>
                <div class="input" :class="{'focus':focusUsername}" placeholder="Username">
                  <el-input @focus="inUsername()" @blur="outUsername()" v-model="userinfo.username" type="text"></el-input>
                </div>
                <div class="input" :class="{'focus':focusPassword}" placeholder="Password">
                  <el-input @focus="inPassword()" @blur="outPassword()" v-model="userinfo.password" type="password" show-password></el-input>
                </div>
                <div class="input" :class="{'focus':focusReward}" placeholder="Reward">
                  <el-input @focus="inReward()" @blur="outReward()" v-model="userinfo.reward" type="password" show-password></el-input>
                </div>
                <div class="input" :class="{'focus':focusVerificationCode}" placeholder="Verification code">
                  <el-input @focus="inVerificationCode()" @blur="outVerificationCode()" v-model="userinfo.verificationCode"></el-input>
                </div>
                <div style="position: relative; margin: 0 1.5rem; top: -0.5rem; text-align: center " >
                  <el-button round style="background-color: #FFFFFF45" @click="getVerificationCode()" :disabled="status">
                    {{ msg }}</el-button>
                </div>
              </div>
              <el-button v-show="Register" class="login__button" type="text" @click="registerUser()" @keyup.enter="registerUser()">Let's go</el-button>
            </el-card>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";

export default {
  name: "Register",
  data(){
    return{
      status: false,
      msg:'获取验证码',
      Register:'1',
      captchaData:"",
      callbackData:'',
      focusEmail:false,
      focusUsername:false,
      focusPassword:false,
      focusReward:false,
      focusVerificationCode:false,
      userinfo:{
        username:'',
        password:'',
        reward:'',
        email:'',
        verificationCode:'',
      },
      bodyHeight: document.documentElement.clientHeight,
      Top: document.documentElement.clientHeight / 4 - 50
    }
  },
  mounted() {
     this.bodyHeight = document.documentElement.clientHeight
  },
  components:{

  },

  methods:{
    getVerificationCode(){
      this.$axios({
        url:"http://127.0.0.1:9999/api/blog/v1/get-verification-code/",
        method:'post',
        data:Qs.stringify({
          email: this.userinfo.email,
        })
      }).then((res) => {
        this.status = true
        this.msg = "已发送"
        console.log(res.data)
      })
    },
    // 输入框焦点事件
    inEmail(){this.focusEmail = true},
    outEmail(){if (this.userinfo.email.length === 0){this.focusEmail = false}else {
      axios({
        url:'http://127.0.0.1:9999/api/blog/v1/uniqueness/',
        method: 'post',
        data: Qs.stringify({
          email: this.userinfo.email,
        })
      }).then((res) =>{
        if (res.data === '邮箱已被注册'){
          this.$message({
          showClose: true,
          message: '邮箱已被注册',
          type: 'error',
          center: true,
        });
        return
        }
      })
    }},
    inUsername(){this.focusUsername = true},
    outUsername(){if (this.userinfo.username.length === 0){this.focusUsername = false}else {
      axios({
        url:'http://127.0.0.1:9999/api/blog/v1/uniqueness/',
        method: 'post',
        data: Qs.stringify({
          username: this.userinfo.username,
        })
      }).then((res) =>{
        if (res.data === '用户名已被使用'){
          this.$message({
          showClose: true,
          message: '用户名已被使用',
          type: 'error',
          center: true,
        });
        return
        }
      })
    }},
    inPassword(){this.focusPassword = true},
    outPassword(){if (this.userinfo.password.length === 0){this.focusPassword = false}},
    inReward(){this.focusReward = true},
    outReward(){if (this.userinfo.reward.length === 0){this.focusReward = false}},
    inVerificationCode(){this.focusVerificationCode = true},
    outVerificationCode(){if (this.verificationCode.length === 0){this.focusVerificationCode = false}},
    goRegister(){
      this.$router.push({name:'Register'})
    },
    goLogin(){
      this.$router.push({name:'Login'})
    },
    // 注册事件
    registerUser(){
      // 邮箱正则
      let email = /^([a-zA-Z]|[0-9])(\w|)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
      // 用户名正则
      let username = /^[a-zA-Z0-9_-]{4,16}$/;
      // 密码正则
      let password = /^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?.]).*$/;
      if (this.userinfo.email.length === 0||
          this.userinfo.username.length === 0||
          this.userinfo.password.length === 0||
          this.userinfo.reward.length === 0 ||
          this.verificationCode === 0
      ){
        this.$message({
          showClose: true,
          message: '请先填写完整',
          type: 'error',
          center: true,
        });
        return
      }
      if (!email.test(this.userinfo.email)){
        this.$message({
          showClose: true,
          message: '邮箱格式错误',
          type: 'error',
          center: true,
        });
        return
      }
      if (!username.test(this.userinfo.username)){
        this.$message({
          showClose: true,
          message: '用户名由4到16位字母，数字或下划线，减号组成',
          type: 'error',
          center: true,
        });
        return
      }
      if (!(password.test(this.userinfo.password) || password.test(this.userinfo.reward))){
        this.$message({
          showClose: true,
          message: '密码至少8位且包含至少一位大小写字母和!@#$%^&*?.特殊符号',
          type: 'error',
          center: true,
        });
        return
      }
      if (this.userinfo.password !== this.userinfo.reward){
        this.$message({
          showClose: true,
          message: '两次密码不一致',
          type: 'error',
          center: true,
        });
        return
      }
      this.$store.dispatch('registerUser', this.userinfo)
    },
  }
}
</script>

<style scoped>
.register{
  height: 100%;
  width: 100vw;
  background: url("../assets/img/IMG_2895-2896.png") center;
  background-size: cover;
}
.register-main{
  position: relative;
}
.navbar{
  position: absolute;
  right: 0;
  padding: 10px 10px;
  z-index: 10;
}
.navbar-register{
  display: flex;
  margin: 0 10px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.navbar-login{
  display: flex;
  margin: 0 10px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.navbar-register p,
.navbar-login p{
  margin: 0 5px;
}
.navbar-register:hover,
.navbar-login:hover{
  color: #ba6a71;
  background-color: #ba6a7140;
  border-radius: 8px;
}
.iconfont{
  font-size: 20px;
  margin: 0 5px;
}
p{
  margin: 0;
  line-height: 30px;
}
.el-col{
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  animation: register_card 1s ease-out 1 forwards;
}
@keyframes register_card {
  0% {
    left:-200px;
  }
  100% {
   left: 50%;
  }
}
.el-card {
  border: 1px solid #7fa9d330;
  background-color: #7fa9d350;
}
.login__card_title{
  text-align: center;
  font-size: 32px;
  font-weight: 600;
  color: #4a5491;
}
/*卡片身体*/
.form .input {
  position: relative;
  margin: 1.5rem;
}
.input::after{
  content: attr(placeholder);
  position: absolute;
  left: 0;
  top: -1%;
  font-size: 1.4rem;
  color: #812b2e;
  transition: all .5s;
  pointer-events:none;
}
.input.focus::after{
  top: -85%;
  transition: all .5s;
  pointer-events:none;
}
.login__button{
  position:relative;
  padding: 5px;
  color: #98789f;
  font-size: 1.5rem;
  left: 50%;
  bottom: 0;
  transform: translate(-50%);
}
/*输入框*/
.register >>> .el-input__inner {
    -webkit-appearance: none;
    background-color: rgba(0, 0, 0, 0);
    background-image: none;
    border: none;
    border-radius: 0;
    border-bottom: .1rem solid #a14840;
    padding: 0 0 0 2px;
    box-sizing: border-box;
    color: #000;
    display: inline-block;
    font-size: 20px;
    height: 30px;
    line-height: 30px;
    outline: none;
}
.register >>> .el-input__inner:focus{
    border-bottom: .1rem solid #a14840;
}
.register >>> .el-input__inner:hover{
    border-color: rgba(0, 0, 0, 0);
    border-bottom: .1rem solid #a14840;
}
/*密码眼睛*/
.register >>> .el-input .el-input__clear:hover {
    color: #a14840;
}
.register >>> .el-input .el-input__clear {
    color: #C0C4CC;
    font-size: 20px;
    cursor: pointer;
    transition: color .2s cubic-bezier(.645,.045,.355,1);
}
.register >>> .el-input__icon {
    height: 100%;
    width: 17px;
    text-align: center;
    transition: all .3s;
    line-height: 30px;
}
</style>