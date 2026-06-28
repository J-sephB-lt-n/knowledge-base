---
created:
  - 2026-05-27T21:46
modified: 2026-05-27 22:33
tags:
type:
  - note
status:
  - in-progress
---
## Example 1 - dotnet learning plan

Model used: `Sonnet 4.6 - medium` (in cursor)

### Example 1 /is_everything_clear
```
<prior model output omitted>
### 4) Questions (prioritized)

1. Should C# language features be included (e.g. async/await, LINQ, nullable reference types, records, generics, attributes)? Or do you only want frameworks and libraries?
    
2. Should the output be structured as a prioritized learning path (e.g. "learn this first, then this") rather than a flat inventory?
    
3. Should each item include a brief contextual note explaining what you need to learn about it and why — or just the name of the concept/library?
    
4. What format do you want the output in — a rich interactive canvas, or a plain markdown response in chat?
   
...

## .NET Learning List for this Codebase (in learning order)

### C# Language

1. Static typing & the type system — C# is statically typed; every variable, parameter, and return value has a declared type. Unlike Python, type errors are caught at compile time.
    
2. Classes, interfaces, and abstract classes — The primary building blocks. Interfaces (`ITemplateService`, `IStorageService`, etc.) are used pervasively to define contracts, with concrete classes injected at runtime.
    
3. Properties (`{ get; set; }`) — C#'s equivalent of Python data attributes with optional accessor logic. Used on every entity, DTO, and config class.
    
4. Namespaces and `using` directives — The module system. `using Services.Template;` is the C# equivalent of `from services import template`.
    
5. Access modifiers — `public`, `private`, `protected`, `internal`. Controls visibility across and within projects/assemblies. `internal` has no Python equivalent — it restricts access to the same DLL.
    
6. Generics — `DbSet<T>`, `IEnumerable<T>`, `Task<T>`, `Result<T>`, `IOptions<T>`. Equivalent to Python generics but enforced at compile time and very widely used here.
    
7. `async` / `await` and `Task<T>` — The async model. Equivalent to Python's `asyncio`, but `Task` replaces `Coroutine`. Nearly every service method here is async.
    
8. LINQ — Query syntax over collections and EF Core: `.Where()`, `.Select()`, `.FirstOrDefault()`, `.ToList()`, `.Any()`, `.Single()`. Think list comprehensions + SQL-style querying, used everywhere.
    
9. Nullable reference types (`?`, `#nullable enable`) — Enabled project-wide. `string?` means the value may be null; `string` means it shouldn't be. The compiler warns on unhandled nulls.
    
10. Attributes — C#'s decorator equivalent: `[Key]`, `[Column]`, `[Authorize]`, `[HttpGet]`, `[Required]`, `[SwaggerOperation]`. Unlike Python decorators, they don't wrap functions — they annotate metadata that frameworks read via reflection.
    
11. Extension methods — Static methods that can be called as if they were instance methods on a type: `this IServiceCollection services`. Used heavily for DI registration (`AddDmpRedis()`) and HttpContext helpers.
    
12. `partial` classes — A single class split across multiple files. `MainDbContext`, `StorageService`, `PlatformContext`, and most generated entities use this.
    
13. Enums — `EntityStatus`, `StorageFileType`, `CloudBlobIncludeTraits`. Strongly typed integer constants with a name.
    
14. Custom exception hierarchy — `UIException`, `EntityNotFoundException` extending `Exception`. Used to communicate domain errors through service layers to controllers.
    
15. `IDisposable` and `using` statements — Resource cleanup. `using var scope = ...` ensures disposal even if an exception is thrown. Equivalent to Python's `with` / `__exit__`.
    
16. `CancellationToken` — Passed into async methods (especially hosted service loops) to support cooperative cancellation. You'll see `stoppingToken` everywhere in background services.
    
17. `partial` methods and source-generated regex — `[GeneratedRegex]` on a `partial` static method (`Base64UnderscoreFilename()` in `StorageRepoFolders.cs`) generates a compiled regex at build time.
    
18. Primary constructors (C# 12) — `public class MyController(ILogger<MyController> logger) : BaseController` — seen on most newer controllers as a shorthand for constructor + field assignment.
    
19. `required` keyword (C# 11) — Forces callers to set a property at object initialisation time. Seen on payload classes like `ExampleApp1Payload`.
    
20. `global using` — A `using` applied to the whole project. `Tests/Web.UnitTests/Usings.cs` shows this — eliminates repeated imports across test files.
    
21. Target-typed `new()` — `List<CurrentFiles> currentFiles = new();` — type is inferred from the left-hand side. Ubiquitous in this codebase.
    
22. Collection expressions (`[...]`) — C# 12: `private static string[] _compareArray => [Native, RabbitMQ];`. Seen in `QueueProviders` and `Clouds`.
    
23. Pattern matching — `switch` expressions, `is`, `as`. Used in storage MIME-type switches and type checks.
    
24. `Span<T>` and `AsSpan()` — Seen in RSA PEM import (`_currentRsa.ImportFromPem(pem.AsSpan())`). Low-allocation slices of memory.
    

---

### .NET Platform & Tooling

25. `dotnet` CLI — `dotnet build`, `dotnet run`, `dotnet test`, `dotnet ef migrations`. The entry point for all development operations.
    
26. NuGet and `.csproj` — Package management and project configuration. `<PackageReference>` is the equivalent of `requirements.txt` entries; `<ProjectReference>` links projects within the solution.
    
27. Solution files (`.sln`) — Groups multiple `.csproj` projects into one build unit. `DataModellingPlatform.sln` is the root.
    
28. `Directory.Build.props` / `Directory.Build.targets` — MSBuild files that apply shared settings (e.g. `Nullable`, `ImplicitUsings`) to all projects in the tree automatically.
    
29. `appsettings.json` and `appsettings.{Environment}.json` — JSON configuration files, loaded automatically by the runtime. `Development` overrides `Production` settings.
    
30. User Secrets — Local-only secrets stored outside the repo (referenced via `UserSecretsId` in `.csproj`). The .NET equivalent of a `.env` file for development.
    
31. `EmbeddedResource` — Files (`.sql`, `.html`, `.pgsql`) baked directly into the DLL. Used for SQL query files in `Services` and HTML email templates.
    
32. `ImplicitUsings` — Auto-imports a set of common namespaces (`System`, `System.Linq`, etc.) project-wide, so they don't need to be stated explicitly.
    

---

### Dependency Injection

33. `Microsoft.Extensions.DependencyInjection` — The built-in DI container. Equivalent to having a global factory/registry. All services are registered here and injected by the framework.
    
34. Service lifetimes: `AddSingleton`, `AddScoped`, `AddTransient` — Singleton = one instance forever; Scoped = one per HTTP request; Transient = new instance each time. Getting this wrong causes subtle bugs.
    
35. Constructor injection — The dominant pattern: the DI container inspects constructor parameters and provides them. You never call `new` on services yourself.
    
36. `IServiceProvider` and manual resolution — Used in hosted services when you need a scoped service from a singleton context: `_serviceProvider.CreateScope()` then `scope.ServiceProvider.GetRequiredService<T>()`.
    
37. Keyed services (`AddKeyedScoped`) — Register multiple implementations of the same interface under different keys. Seen in task worker for poison queue vs. normal queue clients.
    

---

### Configuration & Options Pattern

38. `IConfiguration` — The raw configuration abstraction (reads from `appsettings.json`, env vars, Key Vault, etc.).
    
39. `IOptions<T>` / `IOptionsSnapshot<T>` — Strongly typed configuration objects injected via DI. `IOptions<DmpAppConfig>` gives you a typed config class. `config.Value` accesses the actual values.
    
40. `BindWithAttributes` / `ValidateDataAnnotations` / `ValidateOnStart` — Fluent options registration: bind config to a typed class, validate `[Required]` annotations, and fail fast on startup if invalid.
    
41. `IConfigureOptions<T>` / `IConfigureNamedOptions<T>` — A pattern used here extensively for deferred, DI-aware configuration setup (e.g. `RedisCacheOptionsSetup`, `JwtBearerOptionsSetup`). Lets you configure framework options using other injected services.
    

---

### Logging

42. `ILogger<T>` and `Microsoft.Extensions.Logging` — Structured logging with parameterised messages: `_logger.LogInformation("User {UserId} logged in", userId)`. Equivalent to Python's `logging` module but with structured context.
    
43. `ILoggerFactory` — Creates loggers programmatically (used in RabbitMQ factory adapter to create typed loggers).
    
44. `BeginScope` — Adds ambient key-value context to all log lines within a block. Used in `CorrelationIdMiddleware` to attach a correlation ID to every log line in a request.
    

---

### ASP.NET Core Web API

45. `WebApplication` and `WebApplicationBuilder` — The minimal hosting model entry point (`Program.cs`). `builder` configures services; `app` configures the middleware pipeline.
    
46. Controller-based API — Classes inheriting `ControllerBase` (here via `DmpBaseController`), decorated with `[Route]`, `[HttpGet]`, etc. Return `ActionResult<T>` or `IActionResult`.
    
47. Model binding — `[FromBody]`, `[FromRoute]`, `[FromQuery]` tell ASP.NET Core where to deserialise parameters from. Automatic for most cases.
    
48. Middleware pipeline — `app.UseAuthentication()`, `app.UseAuthorization()`, custom `IMiddleware` classes (`DmpTokenRefresher`, `CorrelationIdMiddleware`). Ordered chain of request handlers.
    
49. `HttpContext` — The per-request object containing request, response, user, items, and service locator. Accessed from middleware and hub methods.
    
50. CORS — Cross-Origin Resource Sharing configuration. `AddCors` + `UseCors` with named policies. Used here for SignalR dev CORS.
    
51. Exception filters (`ExceptionFilterAttribute`) — `UIExceptionFilter` intercepts unhandled `UIException` before the response is sent, returning a 500 with a message.
    
52. Health checks — `AddHealthChecks()`, `AddNpgSql()`, `AddRedis()`, `MapHealthChecks()`. Used for infrastructure readiness endpoints.
    
53. `IHttpClientFactory` — The correct way to create `HttpClient` instances in .NET (avoids socket exhaustion). Seen in test mocks for outbound HTTP calls.
    

---

### Authentication & Authorization

54. JWT Bearer authentication — `AddAuthentication().AddJwtBearer(...)`. The server validates incoming `Authorization: Bearer <token>` headers. Configured via `JwtBearerOptionsSetup`.
    
55. `[Authorize]` and custom `[AuthorizeRole]` — Controller/action-level access control. `AuthorizeRole` is a custom `IAuthorizationFilter` checking a bitmask of roles in the JWT claims.
    
56. `ClaimsPrincipal` and `HttpContext.User` — The authenticated user, with claims (e.g. `sub` = user ID). Parsed from the JWT by the middleware.
    
57. `System.IdentityModel.Tokens.Jwt` — `JwtSecurityTokenHandler` for creating and parsing JWT tokens. Used in the authentication service to issue tokens.
    
58. RSA signing — `System.Security.Cryptography.RSA` for asymmetric JWT signing. The app fetches a PEM public key from Key Vault on startup.
    

---

### Entity Framework Core

59. `DbContext` and `DbSet<T>` — The ORM entry point. `MainDbContext` holds a `DbSet` per table. Equivalent to SQLAlchemy's `Session` + model classes.
    
60. Data annotations on entities — `[Table]`, `[Column]`, `[Key]`, `[ForeignKey]`, `[InverseProperty]`, `[StringLength]`, `[Index]`, `[Keyless]`. Map C# classes to PostgreSQL tables and define relationships.
    
61. Navigation properties — `public virtual Role RoleNavigation { get; set; }` and `public virtual ICollection<MemberRole> MemberRole { get; set; }`. EF Core uses these to load related entities (lazy/eager loading).
    
62. LINQ queries on `DbSet<T>` — `_db.Users.Where(u => u.Id == id).FirstOrDefaultAsync()`. EF Core translates LINQ to SQL.
    
63. Async EF Core operations — `await _db.SaveChangesAsync()`, `await _db.Scheduler.ToListAsync()`. Never call the synchronous versions in an async context.
    
64. Raw SQL migrations — This codebase uses plain `.sql` files in `Migrations/` rather than EF Core code-first migrations. The `Migrations` class reads and applies them manually.
    
65. `Npgsql.EntityFrameworkCore.PostgreSQL` — The PostgreSQL EF Core provider. `UseNpgsql(connectionString)` in `DbContextOptionsBuilder`.
    
66. Testing with in-memory SQLite — `new DbContextOptionsBuilder<MainDbContext>().UseSqlite(":memory:")`. Used in unit tests to avoid needing a real database.
    

---

### Caching

67. `IMemoryCache` — In-process, per-instance cache. Injected and used for short-lived lookups within a single application instance.
    
68. `IDistributedCache` — The abstraction for distributed caching (backed by Redis here). `GetString`, `SetString`, `Refresh` — used in `DmpTokenRefresher` for session management.
    
69. `StackExchange.Redis` — The low-level Redis client. `IConnectionMultiplexer`, `IDatabase`, `HashGet`, `StringSet`, `KeyDelete`. Used directly (bypassing `IDistributedCache`) for richer Redis operations (hashes, pub/sub, etc.).
    

---

### Background Services & Workers

70. `IHostedService` — Implement `StartAsync` / `StopAsync` to run code on application start/stop. `AppInitializer` uses this to run migrations and fetch JWT keys.
    
71. `BackgroundService` — Abstract base class implementing `IHostedService` with a `CancellationToken`-driven `ExecuteAsync` loop. All the `*HostedService` classes here extend it.
    
72. Scoped services from singleton context — Hosted services are singletons but often need scoped services (like `DbContext`). The pattern here is `_serviceProvider.CreateScope()` → `scope.ServiceProvider.GetRequiredService<T>()`.
    
73. Worker process pattern — `Email.Worker` and `Tasks.Worker` are standalone console apps (`<OutputType>Exe</OutputType>`) that run as separate deployable processes, consuming queues in a loop.
    

---

### SignalR

74. `Hub` base class — Real-time bidirectional communication over WebSockets. `CollaborationHub` defines methods clients can invoke, and the hub can push to clients via `Clients.*`.
    
75. Groups — `Groups.AddToGroupAsync`, `Clients.Group(chatId)`. Route messages to subsets of connected clients. Used here to route chat messages to participants.
    
76. Hub client proxy methods — `Clients.Caller.SendAsync("ChatCreated", ...)` calls a JavaScript/client method by name. Strongly typed hub clients are an alternative not used here.
    
77. `ConcurrentDictionary` — Used in the hub to track connection state in a thread-safe way across concurrent WebSocket connections.
    

---

### Swagger / OpenAPI

78. Swashbuckle — Generates OpenAPI docs from controller attributes: `[SwaggerOperation]`, `[SwaggerResponse]`. `UseSwagger()` + `UseSwaggerUI()` exposes the UI.
    
79. `dotnet swagger tofile` — CLI tool (run as a post-build target in `Web.csproj`) that writes the OpenAPI spec to a JSON file for consumption by the Unity frontend.
    

---

### Testing

80. xUnit — The test framework: `[Fact]` for single-case tests, `[Theory]` + `[InlineData]` for parameterised tests. Test classes are instantiated per test (unlike pytest's module scoping).
    
81. Moq — `Mock<IAuthenticationService>()`, `.Setup(m => m.Method()).Returns(...)`, `.Verify(...)`. Equivalent to Python's `unittest.mock.MagicMock`.
    
82. In-memory SQLite for DB tests — `"DataSource=:memory:"` + `EnsureCreated()` creates a fresh throwaway schema per test class. The `IDisposable.Dispose()` closes the connection.
    
83. `coverlet.collector` — Code coverage collection, integrated with `dotnet test`.
    

---

### Azure SDK

84. `Azure.Identity` — `DefaultAzureCredential` authenticates to Azure services using managed identity (in production) or local credentials (in development). No credentials in code.
    
85. `Azure.Storage.Blobs` — `BlobServiceClient`, `BlobContainerClient`, `BlobClient`. Used for blob storage operations (upload, download, list).
    
86. `Azure.Storage.Queues` — Azure Storage Queue client. One of two queue backends (alongside RabbitMQ).
    
87. `Azure.Security.KeyVault.Secrets` / `.Keys` — Reading secrets and cryptographic keys from Azure Key Vault. Used for JWT signing keys and general config secrets.
    
88. `Azure.Extensions.AspNetCore.Configuration.Secrets` — Adds Key Vault as an `IConfiguration` source, so secrets appear as config values transparently.
    
89. `Azure.Monitor.Query` — Log Analytics query client. Used for infrastructure health checks.
    

---

### Google Cloud SDK

90. `Google.Cloud.Storage.V1` — GCS equivalent of Azure Blob Storage. The codebase abstracts both behind a common `ICloudStorageServiceClient` interface.
    
91. `Google.Cloud.SecretManager.V1` — GCP equivalent of Azure Key Vault Secrets.
    
92. `Google.Cloud.Kms.V1` — GCP Key Management Service for JWT signing key retrieval.
    

---

### Messaging

93. `RabbitMQ.Client` — Direct AMQP client. `ConnectionFactory`, `IModel` (channel), `QueueDeclare`, `BasicPublish`, `BasicConsume`, manual ACK. Used as an alternative queue backend.
    
94. Queue abstraction pattern — `IQueueReceiverClient<T>`, `IQueueSenderClient<T>`, `IQueueClientFactory` — internal interfaces that abstract Azure Queues and RabbitMQ behind a common API.
    

---

### Reverse Proxy

95. YARP (`Yarp.ReverseProxy`) — Used in `ExternalApi` to proxy requests. Configured in `appsettings.json` rather than code.

---

### Third-party Libraries

96. `LanguageExt.Core` (`Result<T>`, `Option<T>`, `.Match()`) — A functional programming library heavily used in service return types. `Result<T>` holds either a success value or an exception. `.Match(success => ..., failure => ...)` forces you to handle both cases. This is the most important third-party library to understand for reading service code.
    
97. `System.Text.Json` — The modern .NET JSON serializer. `[JsonPropertyName("model")]`, `JsonSerializer.Serialize/Deserialize`. Used in most new code.
    
98. `Newtonsoft.Json` — The legacy JSON serializer, still used alongside `System.Text.Json` (notably in `AppSettingsApiController` for matching serialisation settings). `JsonConvert.SerializeObject`, `JsonSerializerSettings`.
    
99. `Cronos` — Cron expression parsing library. Used in `SchedulerHostedService` and `SchedulerExecutor` to determine when jobs are due.
    
100. `SixLabors.ImageSharp` — Image processing (resize, convert, WebP encoding via `Shorthand.ImageSharp.WebP`).
    
101. `NPOI` — Excel (`.xlsx`) file reading. `XSSFWorkbook`, `IRow`, `ISheet`. Used in the file validator.
    
102. `Microsoft.Azure.Databricks.Client` — Databricks REST API client. Used to trigger and monitor Databricks jobs.
    
103. `Enums.NET` — Extended enum utilities (display names, conversions). Used in `Common.Web`.
    

---

### Codebase-Specific Patterns

104. `PlatformContext` — The request context object (`AppKey`, `AppId`, `ProjectId`, `UserId`, `Token`) passed as the first argument through most service methods. The C# equivalent of passing a request context dict.
    
105. `DmpBaseController` — The custom base controller. `UserPlatformContext()` extracts a `PlatformContext` from the current HTTP request. All controllers inherit this.
    
106. Interface-per-service pattern — Every service has a corresponding `IXxxService` interface. This is what makes Moq-based testing possible and keeps DI registrations swappable.
    
107. `partial` service classes — `StorageService` is split across `StorageService.cs` and `StorageRepoFolders.cs`. The compiler merges them. Used to keep large service files manageable.
    
108. EmbeddedResource SQL files — SQL queries are stored as `.pgsql` files, compiled into the DLL as embedded resources, then loaded via `Assembly.GetManifestResourceStream()`. Used in `Services` for complex PostgreSQL queries.
    
109. `.resx` resource files — `DataAssetsSqlResource.resx` + auto-generated `DataAssetsSqlResource.Designer.cs`. An older .NET mechanism for accessing named embedded resources via a typed static class.
    

---

### Build & DevOps

110. Docker and multi-stage Dockerfiles — Each deployable (Web, Email.Worker, Tasks.Worker, ExternalApi) has its own `Dockerfile`. Understanding `COPY`, `RUN dotnet publish`, and the two-stage build pattern is necessary to debug deployment issues.
    
111. `docker-bake.hcl` — BuildKit bake files defining multi-image build targets. Used in CI to build all images in one command.
    
112. Azure Pipelines — The CI/CD system (`.yml` files). Each deployable has its own pipeline file (`azure-pipelines-email-worker.yml`, etc.).
    
113. `nuget.config` — Points NuGet at an internal Artifactory feed in addition to nuget.org. Needed to resolve packages in CI and on-boarding.
    
114. Veracode security scanning — Static analysis security tool. `Veracode.props`, `veracode-project.json` configure what gets scanned. Not needed for day-to-day development but relevant when builds are gated on it.
```
### Example 1 GRILL ME
```
Good. I've done a thorough sweep of the codebase. Before building the list and grilling you, I need to calibrate.

Question 1 of N: How much .NET/C# have you been exposed to so far — have you read any C# code, worked through any tutorials, or is this truly a blank slate?

My recommended starting point: assume you've read some C# but haven't written it in anger, so we skip absolute basics (classes, methods, variables) and focus on the concepts that are either genuinely different from Python or non-trivially used in this codebase.

...

Question 2: This codebase has 60+ interfaces (`IProjectService`, `IQueueSenderClient<T>`, etc.) and uses interface-based dependency injection heavily. In Python you'd just pass objects around and rely on duck typing. In Rust you'd use traits. Do you have a mental model of what C# interfaces are and how they differ from both of those, or is that a concept we need to put on the list?

My recommendation: yes, put it on the list — C# interfaces feel closer to Rust traits than Python ABCs, but the DI twist (where you register `IFoo → FooImpl` in a container and the framework injects it for you) is its own concept that Python and Rust don't really have an equivalent for.

...

Question 3: The project system here is quite different from Python. There are 34 `.csproj` files, two `.sln` solution files, and a private NuGet feed on Azure DevOps. In Python you have `requirements.txt` / `pyproject.toml` and you just `pip install`. Do you have any feel for how `.csproj`, `.sln`, and NuGet fit together, or is the entire build/project system a blank slate?

My recommendation: put it on the list — understanding `.csproj` (what it declares, how project references work, how NuGet packages are added) and what a `.sln` file is for are table-stakes before you can add a new project or dependency without breaking things.

...

Question 4: LINQ. This codebase uses it throughout services and EF Core queries. It's a query syntax built into C# that lets you write things like:

var active = projects.Where(p => p.IsActive).Select(p => p.Name).ToList();

Coming from Python you'd write `[p.name for p in projects if p.is_active]`, and from R you'd use `dplyr`. LINQ is the closest C# equivalent but it also drives database queries through EF Core (translates to SQL). Do you have any exposure to LINQ, or is this a blank slate?

My recommendation: definitely on the list, and it has two distinct sub-topics worth separating — LINQ on in-memory collections (lambda syntax, method chaining) and LINQ-to-EF (what translates to SQL vs what silently pulls everything into memory and filters in C#, which is a classic performance trap).

...

Question 5: Attributes. This codebase uses them everywhere — `[Authorize]`, `[FromBody]`, `[Required]`, `[SwaggerOperation]`, custom ones like `[AuthorizeRole]` and `[ConfigKeys]`. In Python these are essentially decorators (`@something`). In Rust they're `#[derive(...)]` / proc macros. Do you have an intuition for what C# attributes are and how they differ (they're metadata attached to code, read at runtime via reflection or by frameworks — they don't execute like Python decorators do), or is that a blank slate?

My recommendation: on the list — the mental model shift is that attributes are inert metadata by default; it's the framework (ASP.NET, the DI container, a validator) that reads them and acts on them. That's not obvious coming from Python decorators which run eagerly at definition time.

...

Question 6: Generics. This codebase uses them heavily — `IQueueSenderClient<TMessage>`, `IAsyncPageableWrapper<T>`, `AddOptions<T>()`, keyed services, etc. You have Rust, so you understand the concept of type-parameterised code. The question is whether you're comfortable with C#'s specific flavour: `where T : class`, covariance/contravariance (`IEnumerable<out T>`), generic constraints, and how generics interact with the DI container (which has its own rules about open vs closed generic registrations). Blank slate on the C# specifics?

My recommendation: put the basics on the list, but you can skip the deep end (variance) initially — the codebase doesn't push covariance/contravariance hard. Focus on generic type constraints and open generic DI registrations, which do appear here.

...

<OMITTED: there ended up being 26 questions in total, all like these ones>

That's everything I needed. Here is the final comprehensive list, ordered by what to learn first, with depth markers:

---

## .NET Learning List for this Codebase

### Foundation — learn these first

1. `dotnet` CLI tooling `[brief]` `dotnet restore`, `build`, `run --project`, `watch`, `add package` and how they map to your Python/pip muscle memory.
    
2. C# language features for a Python developer `[one session]` Extension methods (`this IServiceCollection`), nullable reference types (`string?`, `!`), records, pattern matching (`switch` expressions, `is`), `required` properties, string interpolation (`$"..."`). Extension methods are especially critical — the entire DI registration layer is built on them.
    
3. `.csproj` / `.sln` / NuGet `[one session]` What a project file declares, how project references work, how NuGet packages are added (`dotnet add package`), what a `.sln` is for, and how the private Azure DevOps feed in `nuget.config` is configured.
    
4. C# interfaces and the DI inversion-of-control concept `[one session]` Interfaces vs Python duck typing vs Rust traits. Why `IFoo → FooImpl` registration in a container is different from either, and why this codebase has 60+ interfaces.
    
5. Generics — C# specifics `[brief]` Generic type constraints (`where T : class`), open vs closed generic registrations in the DI container. Your Rust background covers the concept; focus on the C# syntax and DI interaction.
    
6. Attributes `[brief]` Inert metadata vs Python decorators that execute eagerly. How frameworks (ASP.NET, validators, Swagger) read attributes at runtime via reflection.
    
7. `async`/`await` + `Task<T>` + `CancellationToken` `[one session]` Concept transfers from JavaScript; focus on C#-specific sharp edges: `ConfigureAwait(false)`, `async void` danger, `CancellationToken` threading through the call chain, and the difference between `Task.Run` and awaiting an already-async method.
    
8. `IDisposable` / `using` `[brief]` Concept transfers from Python `with`; key point is that the DI container calls `Dispose()` for you on scoped/transient services — almost never call it manually on injected dependencies.
    

---

### Platform fundamentals

9. `Generic Host` + `IHostedService` / `BackgroundService` `[one session]` How the application boots (`Host.CreateApplicationBuilder`), how both the Web API and the workers share the same host model, and how `BackgroundService.ExecuteAsync` is the entry point for workers.
    
10. Dependency Injection container `[one session — the most important item on this list]` `IServiceCollection`, the three lifetimes (`Singleton` / `Scoped` / `Transient`) and their correctness consequences, constructor injection, `IServiceCollection` extension method pattern, and .NET 8 keyed services (`GetKeyedService<T>("key")`).
    
11. IOptions configuration pattern `[one session]` `AddOptions<T>().BindWithAttributes().ValidateDataAnnotations().ValidateOnStart()`, how `appsettings.json` + environment variables flow into strongly-typed POCOs, `IOptions<T>` vs `IOptionsSnapshot` vs `IOptionsMonitor`.
    

---

### ASP.NET Core

12. Middleware pipeline `[one session]` Ordered pipeline in `Startup.cs`, why order matters (auth before authz), the custom middleware shape (`InvokeAsync(HttpContext, RequestDelegate next)`), and what the existing custom middleware (`CorrelationIdMiddleware`, `DmpTokenRefresher`) does.
    
13. Controller-based Web API `[one session]` Attribute routing, `[HttpGet]`/`[HttpPost]`, `[FromBody]`/`[FromQuery]` model binding, `ActionResult<T>` / `IActionResult`, filters vs middleware, and the shared `DmpBaseController` pattern.
    
14. ASP.NET Core JWT auth pipeline `[brief]` `UseAuthentication` vs `UseAuthorization`, how the validated JWT becomes a `ClaimsPrincipal`, `[Authorize]`, and the custom `[AuthorizeRole]` filter. You already know JWT — focus on the wiring.
    
15. Swagger/Swashbuckle `[light touch]` `[SwaggerOperation]`, `[SwaggerResponse]`, XML doc comments on controllers, Bearer security scheme setup. Enough to add documentation to new endpoints.
    

---

### Data

16. LINQ `[one session — two parts]` Part 1: In-memory LINQ — lambda method chaining (`.Where()`, `.Select()`, `.GroupBy()`, `.ToList()`, `.FirstOrDefault()`). Part 2: LINQ-to-EF — what translates to SQL vs what silently pulls everything into memory (the classic N+1 and client-evaluation performance traps).
    
17. EF Core + Npgsql/PostgreSQL `[one session]` `DbContext`, `DbSet<T>`, change tracking, why `DbContext` must be `Scoped` (one per request), deferred query execution, navigation properties and their traps, and this codebase's specific choice of manual `.sql` migrations over EF migrations.
    

---

### Infrastructure (light touch — recognise, not master)

18. Background workers + message queues `[light touch]` `BackgroundService` loop pattern, `IQueueSenderClient<T>` / `IQueueReceiverClient<T>` abstractions, how the API enqueues a task and the worker picks it up. Enough to trace a task end-to-end.
    
19. Redis / `IMemoryCache` / `IDistributedCache` `[light touch]` The difference between in-process and distributed cache, how StackExchange.Redis is wired via DI, `GetOrCreateAsync` pattern.
    
20. `IHttpClientFactory` + typed `HttpClient` `[light touch]` Why `new HttpClient()` is a bug, `AddHttpClient<T>()` registration, and how typed clients are injected and used.
    
21. LanguageExt `Result<T>` / `Option<T>` `[light touch — read to recognise]` `.Match(succ => ..., fail => ...)` syntax. Your Rust background covers the concept; you just need to recognise the C# LanguageExt API and know the codebase convention to unwrap at API boundaries.
```

Notes and conclusion:
1. GRILL_ME asked WAY more questions (26 vs 4 for /is_everything_clear)
2. 
# Example 2 - TODO



## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here