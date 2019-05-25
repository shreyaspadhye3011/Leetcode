require 'sinatra'
require 'sinatra/reloader'
require './comments'
require './students'
# require 'sass'

configure :production do
  DataMapper.setup(:default, ENV['DATABASE_URL'] || "sqlite3://#{Dir.pwd}/main.db") # connecting to db
end

configure :development do
  DataMapper.setup(:default, ENV['DATABASE_URL'] || "sqlite3://#{Dir.pwd}/main.db") # connecting to db
end

configure do
  enable :sessions
  set :session_secrete, 'love'
  set :username, 'test'
  set :password, 'test'
end

get '/login' do
  @title = 'Student Information System - Login'
  erb :login_form
end

post '/login' do
  if params[:username] == settings.username && params[:password] == settings.password
    session[:admin] = true
    erb :logged
  else
    halt(401, 'Incorrect ID/PWD')
    #@failed = true
    #redirect to('/login')
  end
end

get '/logout' do
  session[:admin] = false
  session.clear
  erb :logout
end

get '/' do
  @title = 'Student Information System - Home'
  erb :home
end

get '/about' do
  @title = 'Student Information System - About'
  erb :about_us
end

get '/contact' do
  @title = 'Student Information System - Contact'
  erb :contact
end

get '/video' do
  @title = 'Student Information System - Video'
  erb :videos
end

not_found do
  @title = 'Student Information System - 404 Error'
  erb :notfound
end
