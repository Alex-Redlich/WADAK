<template>
  <div class="ProfileView">
    <div id="Profile">
      <div class="row">
        <div class="col-5">
          <TodayMovie
            v-if="TodayMovie_id"
            :userinfo="this.Userinfo"
            class="d-flex align-items-center justify-content-center"
            style="height: 1500px"
          />
          <div v-else class="d-flex align-items-center justify-content-center" style="height: 1500px">
            <button type="button" class="btn btn-warning btn-lg" style="font-weight: 700" @click="GoSearch">
              오늘의 영화를 고르세요!
            </button>
          </div>
        </div>
        <div class="col-7">
          <div class="row flex-column">
            <div class="d-flex justify-content-center">
              <div class="UserInfo">
                <div id="UserInfo2">
                  <div class="row flex-column align-items-start" style="width: 700px">
                    <div class="d-flex mt-5 align-items-baseline">
                      <p id="chingho">[{{ chinghos }}]</p>
                      <!-- 인벤토리버튼 -->
                      <div>
                        <button v-if="userCheck" id="Btn" class="btn btn-warning" @click="Changechingo">
                          칭호변경
                        </button>
                        <button v-if="userCheck" id="Btn2" class="btn btn-secondary" @click="EditProfile">
                          Edit profile
                        </button>
                        <div v-else>
                          <!-- 본인 프로필이 아니라면 팔로우 버튼 생성 -->
                          <button v-if="isFollowing" id="Btn" class="btn btn-danger" @click="Follow">Cancel</button>
                          <button v-else id="Btn" class="btn btn-primary" @click="Follow">Follow</button>
                        </div>
                      </div>
                    </div>
                    <div class="d-flex">
                      <p id="Nickname">{{ this.Userinfo.nickname }}</p>
                      <img id="levelsymbol" :src="url" alt="" />
                    </div>
                    <div id="UserIntro">
                      <p>{{ this.Userinfo.intro }}</p>
                    </div>
                  </div>
                  <div id="UserCount">
                    <div class="d-flex justify-content-start">
                      <p class="counts">팔로잉 : {{ this.Userinfo.followings_count }}명</p>
                      <p class="counts">팔로워 : {{ this.Userinfo.followers_count }} 명</p>
                    </div>
                    <div class="d-flex justify-content-start">
                      <p class="counts">내 게시글 : {{ this.Userinfo.reviews_count }} 개</p>
                      <p class="counts">내 코멘트 : {{ this.Userinfo.comments_count }} 개</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <h1>최근 좋아한 영화들😍</h1>
            <LikeMovies :userID="userID" />
            <h1>최근 리뷰남긴 영화들🤩</h1>
            <ReviewMovies :userID="userID" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TodayMovie from "@/components/Profile/TodayMovie";
import LikeMovies from "@/components/Profile/LikeMovies";
import ReviewMovies from "@/components/Profile/ReviewMovies";
import axios from "axios";
import Swal from "sweetalert2";

export default {
  name: "ProfileView",
  components: {
    TodayMovie,
    LikeMovies,
    ReviewMovies,
  },
  data() {
    return {
      Userinfo: {},
      userID: this.$store.state.userID, 
      TodayMovie_id: "",
    };
  },
  computed: {
    userCheck() {
      if (this.$store.state.userID === this.Userinfo.id) {
        return true;
      }
      return false;
    },
    followUsers() {
      return this.$store.state.userInteractions.followings;
    },
    isFollowing() {
      if (this.followUsers) {
        for (const followUser of this.followUsers) {
          if (followUser.id === this.Userinfo.id) {
            return true;
          }
        }
      }
      return false;
    },
    chinghos() {
      return this.Userinfo.chingho;
    },
    url() {
      return "/level/" + this.Userinfo.level + ".png";
    },
    isLogin() {
      return this.$store.state.isLogin;
    },
  },
  methods: {
    GoSearch() {
      this.$router.push({ name: "search" });
    },
    Changechingo() {
      const userdata = {
        userID: this.userID,
      };
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1/accounts/chinghopick/",
        data: userdata,
      })
        .then((res) => {
          console.log(res.data);
          this.$router.go(0);
        })
        .catch((err) => console.log(err));
    },
    getUserProfile() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/accounts/profile/${this.$route.params.userID}/`,
      })
        .then((res) => {
          this.Userinfo = res.data;
          this.TodayMovie_id = res.data.today_movie;
        })
        .catch((err) => console.log(err));
    },
    Follow() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/accounts/profile/${this.Userinfo.id}/follow/`,
        data: {
          userID: this.$store.state.userID,
        },
      })
        .then((res) => {
          this.$store.dispatch("UserInteractionUpdate", res.data);
          this.$router.go(0);
        })
        .catch((err) => console.log(err));
    },
    EditProfile() {
      this.$router.push({ name: "update", params: { userID: this.$store.state.userID, Userinfo: this.Userinfo } });
    },
    loginAlert() {
      if (!this.isLogin) {
        Swal.fire("로그인이 필요한 서비스 입니다", "", "error");
        this.$router.push({ name: "login" });
      }
    },
  },
  created() {
    this.loginAlert();
    this.getUserProfile();
    console.log(this.url);
  },
};
</script>
<style scoped>
.ProfileView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  justify-content: center;
  padding-top: 30px;
}
#Profile {
  background-color: white;
  width: 1500px;
  color: #6c6e70;
  border-radius: 30px;
}
.UserInfo {
  display: flex;
  justify-content: start;
  margin-bottom: 30px;
  padding-top: 30px;
}
#chingho {
  font-size: 40px;
  font-weight: 700;
}
#Nickname {
  font-size: 60px;
  font-weight: 1000;
}
#levelsymbol {
  width: 50px;
  height: 50px;
  margin-top: 20px;
  margin-left: 10px;
}
#Btn {
  height: 40px;
  width: 100px;
  margin-left: 10px;
  font-size: 18px;
  color: rgb(255, 255, 255);
}
#Btn2 {
  height: 40px;
  width: 150px;
  margin-left: 10px;
  font-size: 18px;
  color: rgb(255, 255, 255);
}
#UserIntro {
  font-size: 30px;
  text-align: center;
}
.counts {
  margin: 20px;
  margin-left: 0px;
  font-size: 30px;
  font-weight: 700;
}
</style>
